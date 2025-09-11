from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField()