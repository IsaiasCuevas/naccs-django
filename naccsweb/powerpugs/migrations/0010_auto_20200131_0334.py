# Generated by Django 2.2.4 on 2020-01-31 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerpugs', '0009_auto_20200131_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powerpugsiglapplication',
            name='lan',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='powerpugsplayerapplication',
            name='lan',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]