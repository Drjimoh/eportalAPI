# Generated by Django 2.2 on 2019-04-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('ig_handle', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('phone_privacy', models.BooleanField(default=True)),
            ],
        ),
    ]
