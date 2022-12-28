from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=255, null=True)

    def __str__(self) -> str | None:
        return self.department_name
