# Generated by Django 4.1.4 on 2022-12-28 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Department",
            "0009_rename_chartmodel_chart_rename_coursemodel_course_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Term",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("terms_name", models.CharField(max_length=255)),
                ("terms_id", models.IntegerField()),
            ],
        ),
    ]
