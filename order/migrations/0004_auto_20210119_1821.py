# Generated by Django 3.1 on 2021-01-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210118_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('in_delivery', 'In delivery'), ('finished', 'Finished'), ('canceled', 'Canceled')], max_length=20),
        ),
    ]