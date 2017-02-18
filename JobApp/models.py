from django.db import models
from django.contrib.auth.models import User

"""
Job : [Job_id, User_id, title, category, details, location, end_date,
 static_content_type, static_content_path, tags]
category: [Category_id, name, details]
Applications : [user_id, job_id, status]
Interest : [User_id, category_id, strength]
Zipcode : [code, co-ordinates]
Address : [Fields need to be finalised]
"""


class Category(models.Model):
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    choices = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('wip', 'WIP'),
        ('completed', 'Completed')
    )
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    details = models.TextField(max_length=1000)
    status = models.CharField(max_length=10, choices=choices, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    end_date = models.DateField(blank=True, default=None, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=250, blank=True)


    def __str__(self):
        return self.title


class Application(models.Model):
    choices = (
        ('open', 'Open'),
        ('rejected', 'rejected'),
        ('selected', 'selected'),
        ('taken', 'taken'),
        ('closed', 'closed'),
        ('completed', 'completed')
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    status = status = models.CharField(max_length=10, choices=choices, default='open')

    def __str__(self):
        return self.job.slug + " <- " +self.user.username


class Interest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    strength = models.IntegerField()

    def __str__(self):
        return self.category.title + " <> " +self.user.username
