# from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models

"""
Job : [Job_id, User_id, title, category, details, location, end_date, static_content_type, static_content_path, tags]
category: [Category_id, name, details]
Applications : [user_id, job_id, status]
Interest : [User_id, category_id, strength]
Zipcode : [code, co-ordinates]
Address : [Fields need to be finalised]
"""


class Category(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    poly = models.PolygonField()


class Address(models.Model):
    num = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.ForeignKey(Zipcode, null=True, on_delete=models.SET_NULL)
    objects = models.GeoManager()


class Job(models.Model):
    choices = (
        ('open', 'open'),
        ('closed', 'closed'),
        ('wip', 'WIP'),
        ('completed', 'completed')
    )
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    details = models.TextField(max_length=500)
    location = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=choices)


class Application(models.Model):
    choices = (
        ('rejected', 'rejected'),
        ('selected', 'selected'),
        ('taken', 'taken'),
        ('closed', 'closed'),
        ('completed', 'completed')
    )

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    status = status = models.CharField(max_length=10, choices=choices)


class Interest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    strength = models.IntegerField()
