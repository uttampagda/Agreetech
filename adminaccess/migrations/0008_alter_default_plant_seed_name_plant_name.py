# Generated by Django 4.0.4 on 2022-07-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminaccess', '0007_default_plant_name_default_plant_seed_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='default_plant_seed_name',
            name='plant_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
