# Generated by Django 2.2.4 on 2020-01-25 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerpugs', '0005_powerpugsplayerapplication_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='powerpugsplayerapplication',
            name='status',
            field=models.TextField(choices=[('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Denied', 'Denied')], default='Pending'),
        ),
    ]
