# Generated by Django 5.0.4 on 2024-05-05 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0002_alter_batch_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='adress',
            field=models.TextField(default='None'),
        ),
    ]
