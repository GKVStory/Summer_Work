# Generated by Django 3.1.4 on 2021-08-27 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Stu',
        ),
    ]
