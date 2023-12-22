from django.db import models


class Semester(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    max_points = models.IntegerField()

    def __str__(self):
        return self.name
