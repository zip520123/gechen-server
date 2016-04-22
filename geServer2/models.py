from __future__ import unicode_literals
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class ModelFormWithFileField(models.Model):
    upload = models.FileField(upload_to='uploads/')
    
