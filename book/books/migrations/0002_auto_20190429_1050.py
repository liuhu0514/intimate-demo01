# Generated by Django 2.2 on 2019-04-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pic', models.ImageField(upload_to='hotpic')),
            ],
        ),
        migrations.AlterField(
            model_name='stuuser',
            name='sno',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]