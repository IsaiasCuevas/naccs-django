# Generated by Django 2.2.4 on 2019-08-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='collegiate_hub_invite',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]