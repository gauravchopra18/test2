# Generated by Django 2.0.2 on 2018-03-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0007_post_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='msg',
            field=models.CharField(default='', max_length=20),
        ),
    ]
