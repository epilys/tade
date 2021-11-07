# Generated by Django 3.1.3 on 2021-08-03 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tade", "0057_add_context_warnings"),
    ]

    operations = [
        migrations.CreateModel(
            name="Digest",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("active", models.BooleanField(default=False)),
                ("all_stories", models.BooleanField(default=True)),
                ("on_days", models.SmallIntegerField(default=64)),
                ("last_run", models.DateTimeField(blank=True, default=None, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="email_digest",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]