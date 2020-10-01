# Generated by Django 3.0.7 on 2020-06-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=900)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]