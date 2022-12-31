# Generated by Django 4.1.4 on 2022-12-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rules", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resualt",
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
                ("rule_name", models.CharField(max_length=255)),
                ("rule_function", models.CharField(max_length=1024)),
                ("test_function2", models.JSONField(blank=True)),
            ],
        ),
    ]