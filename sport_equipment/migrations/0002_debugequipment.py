# Generated by Django 4.1.4 on 2022-12-15 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sport_equipment", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DebugEquipment",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("sport_equipment.equipment",),
        ),
    ]
