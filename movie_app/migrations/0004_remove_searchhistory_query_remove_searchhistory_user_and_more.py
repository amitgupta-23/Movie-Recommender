# Generated by Django 4.1.7 on 2023-04-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_searchhistory_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchhistory',
            name='query',
        ),
        migrations.RemoveField(
            model_name='searchhistory',
            name='user',
        ),
        migrations.AddField(
            model_name='searchhistory',
            name='username',
            field=models.CharField(default='J', max_length=100),
        ),
    ]
