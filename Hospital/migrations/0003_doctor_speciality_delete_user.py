# Generated by Django 5.1.4 on 2024-12-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(default='Doctor', max_length=100),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
