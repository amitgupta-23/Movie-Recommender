# Generated by Django 4.1.7 on 2023-04-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_remove_searchhistory_query_remove_searchhistory_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
