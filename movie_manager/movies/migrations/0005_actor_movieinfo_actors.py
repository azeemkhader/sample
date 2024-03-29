# Generated by Django 4.2.3 on 2023-12-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_director_movieinfo_directed_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='actors',
            field=models.ManyToManyField(related_name='acted_movies', to='movies.actor'),
        ),
    ]
