# Generated by Django 4.1.5 on 2023-01-19 16:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(db_column='rating', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
        migrations.RemoveField(
            model_name='movie',
            name='name',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_name',
            field=models.CharField(db_column='movie_name', default='ttt', max_length=256),
            preserve_default=False,
        ),
    ]
