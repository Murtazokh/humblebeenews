from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    body_image = models.URLField(null=True, blank=True)

class Sport(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    body_image = models.URLField(null=True, blank=True)



class Politics(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    body_image = models.URLField(null=True, blank=True)  

class Economy(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    body_image = models.URLField(null=True, blank=True)