# Generated by Django 5.1.3 on 2024-12-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_author_alter_post_banner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, default=None, unique=True),
        ),
    ]
