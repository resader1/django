# Generated by Django 5.2.1 on 2025-05-30 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='nickName',
            field=models.CharField(default='없음', max_length=50),
        ),
    ]
