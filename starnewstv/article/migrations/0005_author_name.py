# Generated by Django 5.1.4 on 2025-03-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0004_alter_article_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
