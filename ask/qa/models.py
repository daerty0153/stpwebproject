from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.CharField(max_length=30)
    likes = models.IntegerField()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.TextField()
    author = models.CharField()

