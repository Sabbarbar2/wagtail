# Generated by Django 4.2.4 on 2023-08-14 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("generic", "0004_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="genericpage",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="generic.author",
            ),
        ),
    ]
