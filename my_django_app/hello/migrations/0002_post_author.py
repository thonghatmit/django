# Generated by Django 4.2 on 2023-04-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]