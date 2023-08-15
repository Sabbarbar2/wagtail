# Generated by Django 4.2.4 on 2023-08-15 14:04

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("generic", "0005_genericpage_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("heading", wagtail.blocks.CharBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                ],
                null=True,
                use_json_field=True,
            ),
        ),
    ]