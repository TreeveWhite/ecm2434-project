# Generated by Django 4.0.1 on 2022-02-23 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exeterDomination', '0006_remove_users_lastpos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='claimedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]