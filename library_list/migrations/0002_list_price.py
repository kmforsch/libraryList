# Generated by Django 2.1 on 2018-08-03 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
