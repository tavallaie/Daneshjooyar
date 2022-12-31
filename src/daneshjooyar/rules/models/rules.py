from django.db import models


class Rule(models.Model):
    rule_name = models.CharField(max_length=255)
    rule_function = models.CharField(max_length=1024)
    test_function2 = models.JSONField(blank=True)
