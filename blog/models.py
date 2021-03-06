from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content=models.TextField()
    tags = models.CharField(max_length=10, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    auth_name = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)