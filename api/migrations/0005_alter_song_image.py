# Generated by Django 5.0.7 on 2024-08-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_song_options_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.URLField(max_length=500),
        ),
    ]
