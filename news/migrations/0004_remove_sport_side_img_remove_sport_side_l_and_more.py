# Generated by Django 4.1.4 on 2022-12-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_uzre_img_sport_side_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='side_img',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='side_l',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='side_t',
        ),
        migrations.AddField(
            model_name='sport',
            name='side_img1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sport',
            name='side_l1',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sport',
            name='side_t1',
            field=models.CharField(default='something', max_length=200),
            preserve_default=False,
        ),
    ]
