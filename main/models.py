from django.db import models

from users.models import Cohort, IMUser

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
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name="cohort_class_schedule"),
    venue = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.cohort.name})"

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name="class_attendance_class_schedule")
    date_created = models.DateField()
    date_modified = models.DateField() 
    is_present = models.BooleanField(default=True)
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "class_attendance_attendee"), 
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "cohort_attendance_author")

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


class QueryComment(models.Model):
   
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name="query_comment_query")
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name = "query_comment_author")



