# Generated by Django 3.1.3 on 2021-07-09 17:24

from django.db import migrations


def create_sites(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.all().delete()
    Site.objects.create(domain="localhost", name="tade")  # SITE_ID = 1


class Migration(migrations.Migration):

    dependencies = [
        ("tade", "0031_auto_20210708_1222_squashed_0033_taggregation_description"),
        ("sites", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_sites),
    ]