# Generated by Django 4.2.3 on 2023-12-08 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movieinfo_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=10, null=True)),
                ('certified_by', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='movieinfo',
            name='poster',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='Censor_details',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movies.censorinfo'),
        ),
    ]
