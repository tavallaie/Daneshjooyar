from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_credit = models.IntegerField()
    dependencies = models.ManyToManyField("self", null=True, blank=True)

    def __str__(self) -> str:
        return self.course_name
