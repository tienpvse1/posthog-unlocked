# Generated by Django 3.0.7 on 2020-10-13 13:44

from django.db import migrations, models


def forward(apps, schema_editor):
    User = apps.get_model("posthog", "User")
    for user in User.objects.exclude(toolbar_mode="toolbar"):
        user.toolbar_mode = "toolbar"
        user.save()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0087_fix_annotation_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="toolbar_mode",
            field=models.CharField(
                blank=True,
                choices=[("disabled", "disabled"), ("toolbar", "toolbar")],
                default="toolbar",
                max_length=200,
                null=True,
            ),
        ),
        migrations.RunPython(forward, reverse),
    ]
