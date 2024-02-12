from django.db import models

from inmest.users.models import Cohort, IMUser

# Create your models here.
class ClassSchedule(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    organizer= models.CharField(max_length=50)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE),
    venue = models.TextField()

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_modified = models.DateField() 
    is_present = models.BooleanField(default=True)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE), 
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "cohort_member_author")

class Query(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "query_submitted_by")
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "query_assigned_to")
    resolution_status= [
        ("PENDING", "PENDING"),
        ("IN_PROGRESS", "IN_PROGRESS"),
        ("DECLINED", "DECLINED"),
        ("RESOLVED", "RESOLVED"),
        
    ]
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "query_author")



