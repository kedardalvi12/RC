# Generated by Django 3.0.8 on 2020-08-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0004_auto_20200826_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='phone_no',
            field=models.IntegerField(max_length=10),
        ),
    ]
