# Generated by Django 3.0.7 on 2020-06-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='added_date',
            field=models.DateTimeField(),
        ),
    ]