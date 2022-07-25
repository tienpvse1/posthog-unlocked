# Generated by Django 3.0.3 on 2020-03-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0032_team_multiple_app_urls"),
    ]

    operations = [
        migrations.AlterField(
            model_name="elementgroup", name="hash", field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddConstraint(
            model_name="elementgroup",
            constraint=models.UniqueConstraint(fields=("team", "hash"), name="unique hash for each team"),
        ),
    ]
