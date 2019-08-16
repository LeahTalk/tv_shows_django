from __future__ import unicode_literals
from django.db import models
import datetime


class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "The title must be at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "The network must be at least 3 characters."
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc'] = "The description must be at least 10 characters."
        if postData['date'] > str(datetime.date.today()):
            errors['date'] = "You're not a time traveler"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateField(default=datetime.date.today())
    desc = models.TextField(default = "")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()