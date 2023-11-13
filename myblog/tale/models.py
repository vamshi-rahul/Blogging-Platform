#This is where we create our models for our Blogging Platform.
from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.cascade)
    created_at = models.DataTimeFeild(auto_now_add = True)

    def __str__(self):
        return self.title
        


