# Generated by Django 3.1.3 on 2021-07-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tade', '0006_auto_20210701_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='usename',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]