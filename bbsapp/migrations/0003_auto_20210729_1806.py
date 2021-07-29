# Generated by Django 3.2.3 on 2021-07-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbsapp', '0002_auto_20210729_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='poster',
            field=models.CharField(max_length=10, null=True, verbose_name='评论人'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='comment_num',
            field=models.IntegerField(null=True, verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='like_num',
            field=models.IntegerField(null=True, verbose_name='点赞数'),
        ),
    ]
