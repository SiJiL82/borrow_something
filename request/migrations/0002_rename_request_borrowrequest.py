# Generated by Django 3.2.13 on 2022-04-24 13:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='BorrowRequest',
        ),
    ]
