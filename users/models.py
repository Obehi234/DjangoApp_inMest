from django.db import models

# Create your models here.
from django.db import models


class IMUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    USER_TYPE = [
        ("EIT", "EIT"),
        ("TEACHING_FELLOW", "TEACHING_FELLOW"),
        ("ADMIN_STAFF", "ADMIN_STAFF"),
        ("ADMIN", "ADMIN")
    ]
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)



class Cohort(models.Model):
    name = models.CharField(max_length=30)
    year = models.DateTimeField()
    description = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)


class Query(models.Model):