# Generated by Django 3.2.13 on 2022-05-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_webpage_frequencyofchecking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failure',
            name='FailureTimeFixed',
            field=models.DateTimeField(blank=True),
        ),
    ]