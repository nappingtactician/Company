# Generated by Django 2.2.3 on 2019-07-14 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20190714_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='assetid',
            new_name='assetId',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='taskid',
            new_name='taskId',
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='workerid',
            new_name='workerId',
        ),
    ]
