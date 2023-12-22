from django.db import models
from daneshjooyar.core.models import FieldOfStudy, CourseGroup, Course


class FieldOfStudyCourse(models.Model):
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_group = models.ForeignKey(
        CourseGroup, null=True, blank=True, on_delete=models.SET_NULL
    )
    is_mandatory = models.BooleanField(default=False)
    prerequisites = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="next_courses"
    )
    substitutes = models.ManyToManyField(
        "self", symmetrical=True, blank=True, related_name="substitute_courses"
    )

    class Meta:
        unique_together = ("field_of_study", "course")

    def __str__(self):
        return f"{self.field_of_study} - {self.course} - {'Mandatory' if self.is_mandatory else 'Optional'}"
