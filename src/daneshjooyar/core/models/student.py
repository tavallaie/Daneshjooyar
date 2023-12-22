from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    # Additional fields like email, registration number, etc.

    def __str__(self):
        return self.name
