# Generated by Django 3.2.5 on 2021-08-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firt_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('create_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('create_ad', models.DateTimeField(auto_now_add=True)),
                ('update_ad', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
