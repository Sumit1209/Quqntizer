# Generated by Django 4.1.3 on 2023-01-27 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Discription',
            new_name='discription',
        ),
    ]