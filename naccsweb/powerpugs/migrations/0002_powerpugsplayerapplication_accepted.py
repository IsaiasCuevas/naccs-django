# Generated by Django 2.2.4 on 2020-01-24 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerpugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerpugsplayerapplication',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
