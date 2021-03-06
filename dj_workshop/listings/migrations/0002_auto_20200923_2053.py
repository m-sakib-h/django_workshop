# Generated by Django 2.2.10 on 2020-09-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ('-list_date',)},
        ),
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
