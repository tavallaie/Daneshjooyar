# Generated by Django 4.1.4 on 2022-12-27 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Department", "0003_chartmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="chartmodel",
            name="courses",
            field=models.ManyToManyField(to="Department.coursemodel"),
        ),
    ]
