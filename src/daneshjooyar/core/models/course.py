from django.db import models


class Course(models.Model):
    """
    This model represents the courses offered. Each course has a name,
    points (indicating hours per week), and a flag to indicate if it's a project course
    """

    name = models.CharField(max_length=100)
    points = models.IntegerField(help_text="Number of hours per week")
    is_project = models.BooleanField(default=False)

    def __str__(self):
        return self.name
