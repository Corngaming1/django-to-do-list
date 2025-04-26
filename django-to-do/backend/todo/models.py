from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False) 
    due_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title