# Generated by Django 4.1.5 on 2023-01-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
