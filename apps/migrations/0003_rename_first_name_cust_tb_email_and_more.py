# Generated by Django 4.0.2 on 2022-02-16 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_cust_tb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cust_tb',
            old_name='first_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='cust_tb',
            old_name='last_name',
            new_name='full_name',
        ),
    ]
