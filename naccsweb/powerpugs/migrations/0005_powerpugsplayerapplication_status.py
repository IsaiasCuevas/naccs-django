# Generated by Django 2.2.4 on 2020-01-25 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerpugs', '0004_powerpugsplayerapplication_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='powerpugsplayerapplication',
            name='status',
            field=models.TextField(default='Pending', max_length=25),
        ),
    ]
