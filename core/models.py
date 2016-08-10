from django.db import models

class Card(models.Model):
    serial_number0 = models.IntegerField(max_length=3)
    serial_number1 = models.IntegerField(max_length=3)
    serial_number2 = models.IntegerField(max_length=3)
    serial_number3 = models.IntegerField(max_length=3)
    check_byte = models.IntegerField(max_length=3)

    def __unicode__(self):
        return "Card: %s, %s, %s, %s, %s" % (self.serial_number0,
                                             self.serial_number1,
                                             self.serial_number2,
                                             self.serial_number3,
                                             self.check_byte)

class Owner(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    card_owned = models.ForeignKey(Card)
    access_granted = models.BooleanField(default=False)

    def __unicode__(self):
        return "Owner: %s %s" % (self.first_name, self.last_name)

class Log(models.Model):
    card_detected = models.ForeignKey(Card)
    time_detected = models.DateTimeField()

class RaspberryPiInfo(models.Model):
    hostname = models.CharField(max_length=15, default='255.255.255.255')
    username = models.CharField(max_length=128, default='pi')
    password = models.CharField(max_length=128, default='fuze')

    def __unicode__(self):
        return "Current hostname: %s" % self.hostname
