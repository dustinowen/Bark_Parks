# Generated by Django 4.2.5 on 2023-09-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_picture_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='date',
            field=models.DateField(),
        ),
    ]