# Generated by Django 3.2.6 on 2021-09-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tade", "0081_domain_is_banned"),
    ]

    operations = [
        migrations.AddField(
            model_name="storyremotecontent",
            name="w3m_content",
            field=models.TextField(blank=True, max_length=16384, null=True),
        ),
    ]
