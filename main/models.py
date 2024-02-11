from django.db import models

# Create your models here.
class ClassSchedule(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()

