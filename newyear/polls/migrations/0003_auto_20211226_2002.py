# Generated by Django 3.2.10 on 2021-12-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211226_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text4',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='4:'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text3',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='3:'),
        ),
    ]
