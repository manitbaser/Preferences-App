# Generated by Django 3.0.8 on 2020-08-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('author', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=80)),
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('publish_date', models.DateField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]