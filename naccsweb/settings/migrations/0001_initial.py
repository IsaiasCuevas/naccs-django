# Generated by Django 2.2.4 on 2019-08-26 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraduateFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(blank=True, max_length=80)),
                ('grad_date', models.DateField(blank=True, null=True)),
                ('proof', models.FileField(upload_to='graduate/proof/')),
                ('other', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchoolFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highschool', models.CharField(blank=True, max_length=80)),
                ('college', models.CharField(blank=True, max_length=80)),
                ('grad_date', models.DateField(blank=True, null=True)),
                ('proof', models.FileField(upload_to='highschool/proof/')),
                ('other', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]