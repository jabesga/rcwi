import web
import paramiko
import json

render = web.template.render('templates/')

urls = (
	'/', 'index',
)

#TODO: Be able to change the hostname from the web browser
hostname = '#HOSTNAME'

class index:
	def GET(self):
		return render.index()
	def POST(self):
		print "\t:: Connecting SSH"
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname, username='#USERNAME', password='#PASSWORD')
		din, out, err = ssh.exec_command("sudo python servo2.py")
		web.header('Content-Type', 'application/json')
		if out.readlines()[0].rstrip() == 'Success':
			return json.dumps({'success': True})
		else:
			return json.dumps({'success': False})

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
