# Generated by Django 3.0.2 on 2020-09-22 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('main_title', models.CharField(max_length=255)),
                ('home_link', models.CharField(max_length=255)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]