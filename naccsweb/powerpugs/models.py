from django.db import models
from django.contrib.auth.models import User

from naccsweb.storage_backends import PrivateMediaStorage

IGL_OPTIONS= [
    ('Yes', 'True'),
    ('No', 'False'),
    ]
APP_STATUS= [
    ('Accepted', 'Accepted'),
    ('Pending', 'Pending'),
    ('Denied','Denied')
    ]

class PowerPugsPlayerApplication(models.Model):
    class Meta:
        verbose_name = "Power Pug Player Application"
        verbose_name_plural = "Power Pug Player Applications"
    
    def __str__(self):
        return self.user.profile.nickname
        
    user       = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=80, default="")
    email      = models.CharField(max_length=80)
    college    = models.CharField(max_length=80)
    igl        = models.BooleanField(default=False)
    faceit_link = models.CharField(max_length=80)
    esea_link = models.CharField(max_length=80)
    curr_team = models.CharField(max_length=80, blank=True)
    lan = models.TextField(max_length=1000, blank=True)
    other      = models.TextField(max_length=1000, blank=True)
    application      = models.FileField(upload_to="powerpugs/general/", storage=PrivateMediaStorage())
    paid = models.BooleanField(default=False)
    status      = models.TextField(choices=APP_STATUS, default="Pending")
    accepted = models.BooleanField(default=False)


class PowerPugsIGLApplication(models.Model):
    class Meta:
        verbose_name = "Power Pug IGL Application"
        verbose_name_plural = "Power Pug IGL Applications"
    
    def __str__(self):
        return self.user.profile.nickname
        
    user       = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name       = models.CharField(max_length=80)
    email      = models.CharField(max_length=80)
    faceit_link = models.CharField(max_length=80)
    esea_link = models.CharField(max_length=80)
    curr_team = models.CharField(max_length=80, blank=True)
    lan = models.TextField(max_length=1000, blank=True)
    other      = models.TextField(max_length=1000, blank=True)
    application      = models.FileField(upload_to="powerpugs/igl/", storage=PrivateMediaStorage())
    status      = models.TextField(choices=APP_STATUS, default="Pending")
    accepted = models.BooleanField(default=False)
    