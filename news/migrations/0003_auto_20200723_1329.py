# Generated by Django 3.0.8 on 2020-07-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200723_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='updatetd_a',
        ),
        migrations.AddField(
            model_name='article',
            name='updatetd_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
