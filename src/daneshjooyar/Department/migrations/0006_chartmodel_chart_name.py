# Generated by Django 4.1.4 on 2022-12-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Department", "0005_departmentmodel_department_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="chartmodel",
            name="chart_name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
