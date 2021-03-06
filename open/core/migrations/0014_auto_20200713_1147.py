# Generated by Django 2.2.13 on 2020-07-13 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_fix_demo_fixture"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="activity",
            options={"ordering": ["name"], "verbose_name_plural": "Activities"},
        ),
        migrations.AlterModelOptions(
            name="activitylog",
            options={
                "ordering": ["user", "-time"],
                "verbose_name": "Activity Log",
                "verbose_name_plural": "Activity Logs",
            },
        ),
        migrations.AlterModelOptions(
            name="supplementstackcomposition",
            options={"verbose_name": "Supplement Stack Composition"},
        ),
    ]
