# Generated by Django 4.0.1 on 2022-02-16 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exeterDomination', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='possession',
        ),
    ]
