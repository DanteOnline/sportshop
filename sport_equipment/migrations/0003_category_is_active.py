# Generated by Django 4.1.4 on 2022-12-12 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sport_equipment", "0002_equipment_is_own_shop"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
