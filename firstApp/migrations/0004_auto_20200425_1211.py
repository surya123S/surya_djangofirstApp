# Generated by Django 2.2.7 on 2020-04-25 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_auto_20200425_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='frist_name',
            new_name='first_name',
        ),
    ]
