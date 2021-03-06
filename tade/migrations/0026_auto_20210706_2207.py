# Generated by Django 3.1.3 on 2021-07-06 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tade", "0025_hat_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="StoryBookmark",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("annotation", models.TextField(blank=True, null=True)),
                (
                    "story",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tade.story"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CommentBookmark",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("annotation", models.TextField(blank=True, null=True)),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tade.comment"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="saved_comments",
            field=models.ManyToManyField(
                blank=True,
                related_name="saved_by",
                through="tade.CommentBookmark",
                to="tade.Comment",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="saved_stories",
            field=models.ManyToManyField(
                blank=True,
                related_name="saved_by",
                through="tade.StoryBookmark",
                to="tade.Story",
            ),
        ),
    ]
