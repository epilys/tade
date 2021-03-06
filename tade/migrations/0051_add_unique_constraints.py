# Generated by Django 3.1.3 on 2021-07-22 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tade", "0050_invitationrequest_invitationrequestvote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invitation",
            name="address",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="invitationrequestvote",
            name="request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="votes",
                to="tade.invitationrequest",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="hat",
            unique_together={("user", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="vote",
            unique_together={("user", "story", "comment")},
        ),
    ]
