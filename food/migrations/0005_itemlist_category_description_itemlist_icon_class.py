# Generated by Django 5.0.6 on 2025-04-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0004_alter_items_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="itemlist",
            name="category_description",
            field=models.TextField(default="Default description", max_length=255),
        ),
        migrations.AddField(
            model_name="itemlist",
            name="icon_class",
            field=models.CharField(default="fa-solid fa-utensils", max_length=100),
        ),
    ]
