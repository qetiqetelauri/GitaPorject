# Generated by Django 4.0.4 on 2022-04-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theTwitter', '0003_post_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
