# Generated by Django 4.0.4 on 2022-05-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hateApp', '0002_rename_members_hateapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='hateapp',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hateapp',
            name='hatefood',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]