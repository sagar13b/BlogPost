# Generated by Django 2.2.5 on 2019-10-04 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_user_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]