# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number0', models.IntegerField(max_length=3)),
                ('serial_number1', models.IntegerField(max_length=3)),
                ('serial_number2', models.IntegerField(max_length=3)),
                ('serial_number3', models.IntegerField(max_length=3)),
                ('check_byte', models.IntegerField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_detected', models.DateTimeField()),
                ('card_detected', models.ForeignKey(to='core.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('access_granted', models.BooleanField(default=False)),
                ('card_owned', models.ForeignKey(to='core.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RaspberryPiInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(default=b'255.255.255.255', max_length=15)),
                ('username', models.CharField(default=b'pi', max_length=128)),
                ('password', models.CharField(default=b'fuze', max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
