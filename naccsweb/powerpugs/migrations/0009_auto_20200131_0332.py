# Generated by Django 2.2.4 on 2020-01-31 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerpugs', '0008_powerpugsplayerapplication_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powerpugsiglapplication',
            name='lan',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='powerpugsplayerapplication',
            name='lan',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
