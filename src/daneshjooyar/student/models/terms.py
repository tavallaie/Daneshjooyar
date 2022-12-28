from django.db import models
from student.models import StudentProfile
from Department.models import Term, Course


class Terms(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self) -> str:
        return self.term.terms_name
