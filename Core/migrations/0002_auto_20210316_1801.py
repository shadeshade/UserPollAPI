# Generated by Django 2.2.10 on 2021-03-16 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
