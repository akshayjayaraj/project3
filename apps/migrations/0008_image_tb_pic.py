# Generated by Django 4.0.2 on 2022-03-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_rename_imgage_tb_image_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_tb',
            name='pic',
            field=models.ImageField(default=0, upload_to='picture'),
            preserve_default=False,
        ),
    ]
