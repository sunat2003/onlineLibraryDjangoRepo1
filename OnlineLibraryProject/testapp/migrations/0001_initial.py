# Generated by Django 4.0 on 2024-05-31 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('pages', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Magagin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('publish_date', models.DateField()),
                ('article', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NewsPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('headline', models.TextField(max_length=30)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]
