from django.db import models

# Create your models here.

class User(models.Model):

    user_id = models.IntegerField()
    user_name = models.CharField(max_length = 128)

class ActivityPeriod(models.Model):

    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    tz = models.CharField(max_length = 64)
    activity_period = models.TextField()
