# Generated by Django 2.0.3 on 2018-03-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='playlist',
            field=models.ManyToManyField(blank=True, null=True, to='login.PlayList'),
        ),
    ]
