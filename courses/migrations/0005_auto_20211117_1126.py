# Generated by Django 3.2.8 on 2021-11-17 05:56

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='video_url',
        ),
        migrations.AddField(
            model_name='lesson',
            name='url',
            field=embed_video.fields.EmbedVideoField(default='https://youtu.be/cdbJv7amERc'),
        ),
    ]
