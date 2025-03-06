# Generated by Django 5.1.4 on 2025-03-04 02:34

import django.db.models.deletion
import shortuuidfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MenuItems",
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
                (
                    "idx",
                    shortuuidfield.fields.ShortUUIDField(
                        blank=True, editable=False, max_length=22, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("label", models.CharField(max_length=100)),
                ("url", models.CharField(max_length=100)),
                (
                    "psition",
                    models.CharField(
                        choices=[
                            ("header", "Header"),
                            ("footer", "Footer"),
                            ("sidebar", "Sidebar"),
                        ],
                        default="header",
                        max_length=20,
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="store.menuitems",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
