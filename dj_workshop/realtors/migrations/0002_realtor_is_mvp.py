# Generated by Django 2.2.10 on 2020-09-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='is_mvp',
            field=models.BooleanField(default=False),
        ),
    ]
