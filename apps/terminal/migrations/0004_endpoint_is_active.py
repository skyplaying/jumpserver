# Generated by Django 4.1.13 on 2024-09-25 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0003_auto_20171230_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]