# Generated by Django 4.0.4 on 2022-05-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
      
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]