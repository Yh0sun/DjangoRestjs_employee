# Generated by Django 3.1.13 on 2022-05-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emailId',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
