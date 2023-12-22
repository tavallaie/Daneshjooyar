from django.db import models
from daneshjooyar.core.models import FieldOfStudy


class CourseGroup(models.Model):
    """
    Course groups are collections of courses within a Field of Study. They can have
    minimum point requirements (e.g., students must take at least 4 points from this group).
    """

    name = models.CharField(max_length=100)
    min_points = models.IntegerField(null=True, blank=True)
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.field_of_study} - {self.name}"
