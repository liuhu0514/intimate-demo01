# Generated by Django 2.2 on 2019-04-16 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=20)),
                ('tsubject', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='StuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sage', models.IntegerField()),
                ('sgender', models.BooleanField()),
                ('sclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest02.ClassInfo')),
            ],
        ),
        migrations.AddField(
            model_name='classinfo',
            name='ctea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest02.TeaInfo'),
        ),
    ]
