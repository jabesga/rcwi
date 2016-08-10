from django.shortcuts import render, HttpResponse
import json
import pysftp
from models import RaspberryPiInfo, Log, Owner, Card

def index(request):
    return render(request, 'core/index.html')

def logs(request):
    last_ten_logs = Log.objects.all().order_by('-id')[:10]
    info_ten_logs = []
    for log in last_ten_logs:
        owner = log.card_detected.owner_set.all()
        list_element = []
        if owner:
            owner_name = owner[0].first_name + ' ' + owner[0].last_name
        else:
            owner_name = ''
        list_element.append(owner_name)
        list_element.append(log.card_detected)
        list_element.append(log.time_detected)
        info_ten_logs.append(list_element)
  
    return render(request, 'core/last_logs.html', {'info_ten_logs': info_ten_logs })

def card(request, card_id):
    card_info = Card.objects.get(pk=card_id)
    return render(request, 'core/card_info.html', {'card_info': card_info})

def owner(request, owner_id):
    owner_info = Owner.objects.get(pk=owner_id)
    card_owned = Card.objects.get(pk=owner_info.card_owned.id)
    return render(request, 'core/owner_info.html', {'owner_info': owner_info, 'card_owned': card_owned})

def gate_controls(request):
    return render(request, 'core/gate_controls.html')

def up_door(request):
    if request.method == 'POST':
        command = "sudo python /home/pi/SPI-Py/MFRC522-python/upDoor_cmd.py"
        try:
            d = RaspberryPiInfo.objects.get(id=1)

            with pysftp.Connection(d.hostname, username=d.username, password=d.password, port=2200) as sftp:
                sftp.execute(command)
            response_data = {'success': True}

        except pysftp.ConnectionException:
            response_data = {'success': False}
        except pysftp.SSHException:
            response_data = {'success': False}

        return HttpResponse(json.dumps(response_data), content_type="application/json")

def down_door(request):
    if request.method == 'POST':
        command = "sudo python /home/pi/SPI-Py/MFRC522-python/downDoor_cmd.py"
        try:
            d = RaspberryPiInfo.objects.get(id=1)
            with pysftp.Connection(d.hostname, username=d.username, password=d.password, port=2200) as sftp:
                sftp.execute(command)
                response_data = {'success': True}
            

        except pysftp.ConnectionException:
            response_data = {'success': False}
        except pysftp.SSHException:
            response_data = {'success': False}

        return HttpResponse(json.dumps(response_data), content_type="application/json")



def add_owner(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        card_owned = request.POST.get('card_owned')
        access_granted = request.POST.get('access_granted')
        command = "sudo python /home/pi/SPI-Py/MFRC522-python/add_owner.py '%s' '%s' '%s' '%s'" % (first_name, last_name, card_owned, access_granted)
        try:
            d = RaspberryPiInfo.objects.get(id=1)

            with pysftp.Connection(d.hostname, username=d.username, password=d.password, port=2200) as sftp:
                sftp.execute(command)
            response_data = {'success': True}

        except pysftp.ConnectionException:
            response_data = {'success': False}
        except pysftp.SSHException:
            response_data = {'success': False}

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render(request, 'core/add_owner.html')

def open_gate(request):
    if request.method == 'POST':
        try:
            d = RaspberryPiInfo.objects.get(id=1)

            with pysftp.Connection(d.hostname, username=d.username, password=d.password) as sftp:
                sftp.execute('sudo python servo2.py')
            response_data = {'success': True}

        except pysftp.ConnectionException:
            response_data = {'success': False}
        except pysftp.SSHException:
            response_data = {'success': False}

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse()

def manual_update_ip(request):
    d = RaspberryPiInfo.objects.get(id=1)

    if request.method == 'POST':
        hostname = '.'
        numbers = (request.POST['hostname1'],
                   request.POST['hostname2'],
                   request.POST['hostname3'],
                   request.POST['hostname4'])

        d.hostname = hostname.join(numbers)
        d.save()
        return render(request, 'core/request-ip.html', {'current_hostname': d.hostname, 'response': True})

    else:
        return render(request, 'core/request-ip.html', {'current_hostname': d.hostname})

