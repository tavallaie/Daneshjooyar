from django.db import models
from django.contrib.auth.models import User
from Department.models import department, Chart, Course


class StudentProfile(models.Model):
    student_id = models.CharField(max_length=255, default="not provided")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_chart = models.ForeignKey(Chart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.student_id
