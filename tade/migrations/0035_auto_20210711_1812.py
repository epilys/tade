# Generated by Django 3.1.3 on 2021-07-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tade", "0034_user_avatar_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="github_username",
        ),
        migrations.AddField(
            model_name="user",
            name="git_repository",
            field=models.URLField(blank=True, null=True),
        ),
    ]