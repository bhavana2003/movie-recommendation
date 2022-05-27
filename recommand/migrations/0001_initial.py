# Generated by Django 4.0.4 on 2022-05-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.CharField(max_length=1000)),
                ('img', models.ImageField(upload_to='pics')),
                ('age', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('rating', models.FloatField()),
                ('genre1', models.CharField(max_length=20)),
                ('genre2', models.CharField(max_length=20)),
                ('genre3', models.CharField(max_length=20)),
            ],
        ),
    ]
