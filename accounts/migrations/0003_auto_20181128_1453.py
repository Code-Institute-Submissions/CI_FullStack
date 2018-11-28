# Generated by Django 2.1.3 on 2018-11-28 14:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_profilemodel_twitter_handle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileModel',
            new_name='Profile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profile_img',
            new_name='profile_image',
        ),
    ]