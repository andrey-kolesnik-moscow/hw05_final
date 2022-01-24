# Generated by Django 2.2.16 on 2022-01-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_follow'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_subscribers_and_authors'),
        ),
    ]
