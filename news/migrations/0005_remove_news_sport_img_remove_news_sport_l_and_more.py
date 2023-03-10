# Generated by Django 4.1.4 on 2022-12-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_sport_side_img_remove_sport_side_l_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='sport_img',
        ),
        migrations.RemoveField(
            model_name='news',
            name='sport_l',
        ),
        migrations.RemoveField(
            model_name='news',
            name='sport_t',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='bbc_img',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='bbc_l',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='bbc_t',
        ),
        migrations.AddField(
            model_name='sport',
            name='sport_img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sport',
            name='sport_l',
            field=models.TextField(default='s'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sport',
            name='sport_t',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
