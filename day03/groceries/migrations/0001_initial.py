# Generated by Django 5.1.4 on 2025-01-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=35)),
                ('Brand', models.CharField(max_length=30)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
