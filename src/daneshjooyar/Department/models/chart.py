from django.db import models
from Department.models import Department
from Department.models import Course


class Chart(models.Model):
    """Chart  model use for specifying Charts for each department and courses inclouded"""

    chart_name = models.CharField(max_length=255, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self) -> str | None:

        return self.chart_name
