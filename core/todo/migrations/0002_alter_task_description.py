# Generated by Django 4.2.10 on 2024-07-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
