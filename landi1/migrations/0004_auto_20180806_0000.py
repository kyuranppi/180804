# Generated by Django 2.0 on 2018-08-05 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landi1', '0003_auto_20180805_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='clicked_date',
            new_name='scraped_date',
        ),
    ]
