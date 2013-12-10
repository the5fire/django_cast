#coding:utf-8

from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Cast(models.Model):
    title = models.CharField(max_length=200)
    url = models.FileField(upload_to="static/data", storage=FileSystemStorage(), verbose_name=u'URL')

    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
