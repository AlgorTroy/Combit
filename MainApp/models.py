from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
# Create your models here


class Tile(models.Model):
    title = models.CharField(blank=True, max_length=100)
    open_jobs = models.IntegerField(blank=True, null=True)
    short_desc = models.CharField(blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User)
