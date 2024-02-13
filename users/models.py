from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class IMUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    USER_TYPE_CHOICES = [
        ("EIT", "EIT"),
        ("TEACHING_FELLOW", "TEACHING_FELLOW"),
        ("ADMIN_STAFF", "ADMIN_STAFF"),
        ("ADMIN", "ADMIN")
    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"



class Cohort(models.Model):
    name = models.CharField(max_length=30)
    year = models.DateTimeField()
    description = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name="cohort_author")

    def __str__(self):
        return self.name


class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name="cohort")
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name="cohort_member")
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name="cohort_member_author")

    def __str__(self):
        return f"{self.member} - {self.cohort}"


