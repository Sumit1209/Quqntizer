# Generated by Django 4.1.3 on 2023-01-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_discription_contact_discription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=80)),
                ('subheading', models.CharField(max_length=150)),
            ],
        ),
    ]