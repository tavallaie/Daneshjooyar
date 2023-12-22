from django.db import models


class FieldOfStudy(models.Model):
    """
    This model represents different fields of study (like Computer Science, Mathematics, etc.) in the school.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
