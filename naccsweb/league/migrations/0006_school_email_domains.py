# Generated by Django 2.2.4 on 2019-10-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_school_main_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='email_domains',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
