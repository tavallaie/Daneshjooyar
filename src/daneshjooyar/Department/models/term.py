from pyexpat import model
from django.db import models


class Term(models.Model):
    terms_name = models.CharField(max_length=255)
    terms_id = models.IntegerField()
