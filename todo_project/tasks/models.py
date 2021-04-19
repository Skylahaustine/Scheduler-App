from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Tasks(models.Model):
    
    body= models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]

    def get_absolute_url(self):
        return reverse('task_list')