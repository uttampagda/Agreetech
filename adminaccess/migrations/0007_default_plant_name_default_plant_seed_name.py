# Generated by Django 4.0.4 on 2022-07-12 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminaccess', '0006_remove_fertilizer_crop_days_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default_plant_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Default_plant_seed_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed_name', models.CharField(max_length=50)),
                ('plant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminaccess.default_plant_name')),
            ],
        ),
    ]
