from django.db import models
from core.models import Student, Course


class CompletedCourse(models.Model):
    student = models.ForeignKey(
        Student, related_name="completed_courses", on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, related_name="completed_by_students", on_delete=models.CASCADE
    )
    gpa = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
