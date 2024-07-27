# Generated by Django 5.0.7 on 2024-07-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('cooking_time', models.IntegerField()),
                ('ingredients', models.TextField()),
            ],
        ),
    ]
