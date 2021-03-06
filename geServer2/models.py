from __future__ import unicode_literals
from django.db import models
import os
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    pass

class ModelFormWithFileField(models.Model):
    upload = models.FileField()
    def filename(self):
        return os.path.basename(self.upload.name)
