# Generated by Django 5.2.1 on 2025-05-26 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuscore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuscore',
            name='avg',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stuscore',
            name='eng',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stuscore',
            name='kor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stuscore',
            name='math',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stuscore',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
