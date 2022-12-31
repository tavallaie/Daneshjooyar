from django.db import models
from rules.models import Rule


class Result(models.Model):
    resualt_name = models.CharField(max_length=255)
    rule_function = models.ManyToManyField(Rule)
