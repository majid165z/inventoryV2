# Generated by Django 3.2.21 on 2023-09-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='technical',
            field=models.BooleanField(default=False, verbose_name='بخش فنی (متقاضی)'),
        ),
    ]
