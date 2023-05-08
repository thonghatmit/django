from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=10000000)
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    '''
    def __init__(self,title,body,created_at):
  
     self.title = title       
     self.body= body
     self.created_at=created_at
     '''
