# Generated by Django 5.1.4 on 2024-12-27 22:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('rewards_points', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
