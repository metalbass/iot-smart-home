# Generated by Django 3.0.3 on 2020-02-16 23:36

import collectionfield.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20200217_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='traits',
        ),
        migrations.AddField(
            model_name='device',
            name='traits',
            field=collectionfield.models.fields.CollectionField(choices=[('action.devices.traits.OnOff', 'On Off')], collection_type=set, unique=True),
        ),
    ]
