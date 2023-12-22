from django.db import models
from core.models import Student, Semester


class StudentSemester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    max_points = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ("student", "semester")

    def __str__(self):
        return f"{self.student.name} - {self.semester.name}"
