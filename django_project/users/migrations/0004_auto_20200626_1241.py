# Generated by Django 3.0.7 on 2020-06-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Bio',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]