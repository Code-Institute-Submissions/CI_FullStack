# Generated by Django 2.1.3 on 2018-12-13 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181213_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
