# Generated by Django 4.0.4 on 2022-09-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminaccess', '0009_default_pesticide_avarage_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesticide',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
