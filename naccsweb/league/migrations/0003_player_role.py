# Generated by Django 2.2.4 on 2019-10-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0002_school_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='role',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]