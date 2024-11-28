from django.db import models


class students(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default="M", null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=20, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')
