# Generated by Django 4.1.4 on 2022-12-21 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_economy_uza_img_economy_uza_l_economy_uza_t'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='matbuot_img',
        ),
        migrations.RemoveField(
            model_name='news',
            name='matbuot_l',
        ),
        migrations.RemoveField(
            model_name='news',
            name='matbuot_t',
        ),
        migrations.RemoveField(
            model_name='news',
            name='uza_img',
        ),
        migrations.RemoveField(
            model_name='news',
            name='uza_l',
        ),
        migrations.RemoveField(
            model_name='news',
            name='uza_t',
        ),
        migrations.AddField(
            model_name='economy',
            name='aniq_img',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='economy',
            name='aniq_l',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='economy',
            name='aniq_t',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
