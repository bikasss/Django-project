# Generated by Django 3.0.7 on 2020-06-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profession',
            field=models.CharField(max_length=100),
        ),
    ]
