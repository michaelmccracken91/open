# Generated by Django 2.2.4 on 2019-08-10 06:24

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    dependencies = [("core", "0002_writeup_prompt_models_refactored")]

    operations = [
        migrations.AlterModelOptions(
            name="writeupflaggedprompt",
            options={"verbose_name": "Write Up Flagged Prompt"},
        ),
        migrations.AlterModelOptions(
            name="writeupprompt", options={"verbose_name": "Write Up Prompt"}
        ),
        migrations.AlterModelOptions(
            name="writeuppromptvote", options={"verbose_name": "Write Up Prompt Vote"}
        ),
        migrations.AddField(
            model_name="writeupprompt",
            name="score",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="writeupprompt",
            name="share_state",
            field=django_fsm.FSMField(
                choices=[
                    ("unshared", "Unshared"),
                    ("published_link_access_only", "Link Access Only"),
                    ("published", "Published"),
                ],
                default="unshared",
                max_length=50,
            ),
        ),
    ]
