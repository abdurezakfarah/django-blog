# Generated by Django 5.1.3 on 2024-12-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                ("body", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]