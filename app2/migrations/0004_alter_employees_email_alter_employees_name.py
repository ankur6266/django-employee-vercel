# Generated by Django 4.2 on 2023-04-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0003_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
