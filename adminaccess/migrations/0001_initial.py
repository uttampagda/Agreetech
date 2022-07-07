# Generated by Django 4.0.4 on 2022-07-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop_selling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('farm_id', models.IntegerField()),
                ('harvesting_id', models.IntegerField()),
                ('sell_quantity', models.IntegerField()),
                ('sell_date', models.DateTimeField(auto_now_add=True)),
                ('sell_rate', models.IntegerField()),
                ('purchaser_name', models.CharField(max_length=50)),
                ('purchaser_number', models.IntegerField()),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farm_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('farm_nick_name', models.CharField(blank=True, max_length=50, null=True)),
                ('farm_space', models.IntegerField(blank=True, null=True)),
                ('geo_location', models.CharField(blank=True, max_length=50, null=True)),
                ('farm_village', models.CharField(blank=True, max_length=50, null=True)),
                ('khata_no', models.CharField(blank=True, max_length=50, null=True)),
                ('who_caretaker', models.CharField(blank=True, max_length=50, null=True)),
                ('caretaker', models.CharField(blank=True, max_length=50, null=True)),
                ('caretaker_phone_number', models.IntegerField(blank=True, null=True)),
                ('soil_type', models.CharField(blank=True, max_length=50, null=True)),
                ('water_source', models.CharField(blank=True, max_length=50, null=True)),
                ('water_type', models.CharField(blank=True, max_length=50, null=True)),
                ('water_season', models.CharField(blank=True, max_length=50, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('address', models.TextField()),
                ('aadhar_number', models.IntegerField(blank=True, null=True)),
                ('family_members', models.IntegerField(blank=True, null=True)),
                ('family_occupation', models.CharField(blank=True, max_length=50, null=True)),
                ('is_access', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('farm_id', models.IntegerField()),
                ('planting_id', models.IntegerField()),
                ('fertilizer_name', models.CharField(max_length=50)),
                ('fertilizer_qty', models.CharField(max_length=50)),
                ('fertilizer_qty_per_acre', models.CharField(max_length=50)),
                ('fertilizer_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('crop_days', models.CharField(max_length=50)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Harvesting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('farm_id', models.IntegerField()),
                ('planting_id', models.IntegerField()),
                ('plant_type', models.CharField(max_length=50)),
                ('harvesting_time', models.CharField(max_length=50)),
                ('total_production', models.IntegerField()),
                ('per_acre_production', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pesticide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('farm_id', models.IntegerField()),
                ('planting_id', models.IntegerField()),
                ('pesticide_name', models.CharField(max_length=50)),
                ('pesticide_qty', models.CharField(max_length=50)),
                ('pesticide_date', models.DateTimeField(auto_now_add=True)),
                ('pesticide_days', models.CharField(blank=True, max_length=50, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Planting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('farm_id', models.IntegerField()),
                ('planting_time', models.CharField(blank=True, max_length=50, null=True)),
                ('plant', models.CharField(max_length=50)),
                ('plant_type', models.CharField(max_length=50)),
                ('planting_area', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Soil_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('farm_id', models.IntegerField()),
                ('test_year', models.IntegerField()),
                ('soil_test', models.CharField(blank=True, max_length=50, null=True)),
                ('water_test', models.CharField(blank=True, max_length=50, null=True)),
                ('nitrogen', models.CharField(blank=True, max_length=50, null=True)),
                ('phosphorus', models.CharField(blank=True, max_length=50, null=True)),
                ('potassium', models.CharField(blank=True, max_length=50, null=True)),
                ('other_element', models.CharField(blank=True, max_length=50, null=True)),
                ('test_file', models.FileField(blank=True, null=True, upload_to='<django.db.models.fields.IntegerField>/soil_test')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Water_irrigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('farm_id', models.IntegerField()),
                ('planting_id', models.IntegerField()),
                ('water_irrigation_type', models.CharField(blank=True, max_length=50, null=True)),
                ('crop_days', models.CharField(blank=True, max_length=50, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
