# Generated by Django 3.2.8 on 2021-11-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20211107_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='grade',
            field=models.IntegerField(default=6),
        ),
    ]