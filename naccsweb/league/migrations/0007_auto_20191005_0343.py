# Generated by Django 2.2.4 on 2019-10-05 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_school_email_domains'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='email_domains',
            new_name='email_domain',
        ),
    ]
