# Generated by Django 2.2.4 on 2020-04-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200419_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
