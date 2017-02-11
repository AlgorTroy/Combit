from mongoengine import *
import datetime


connect('CombitDb')
class User(Document):
    email = StringField(required=True)
    user_name = StringField(max_length=50, required=True)
    password = StringField(max_length=50)
    location =  GeoPointField()
    rating = IntField()
    created_date = DateTimeField()
    is_active = BooleanField(default=False)


""" HINTS:
User("test@mail.com", "abc", "xyz", [21.1232,23.23432], 10, datetime.datetime.now(), True).save()
"""
