# Generated by Django 2.2 on 2019-04-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
