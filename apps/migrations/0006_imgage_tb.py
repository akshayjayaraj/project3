# Generated by Django 4.0.2 on 2022-03-02 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_cust_tb_number_cust_tb_first_name_cust_tb_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgage_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='picture')),
            ],
        ),
    ]