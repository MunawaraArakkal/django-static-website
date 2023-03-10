# Generated by Django 4.1.7 on 2023-02-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('det', models.TextField()),
            ],
        ),
    ]
