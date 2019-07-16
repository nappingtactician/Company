# Generated by Django 2.2.3 on 2019-07-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_auto_20190714_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='allocatework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetId', models.CharField(max_length=25)),
                ('taskId', models.CharField(max_length=25)),
                ('workerId', models.CharField(max_length=25)),
                ('timeOfAllocation', models.CharField(max_length=25)),
                ('taskToBePerformedBy', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='asset_desc',
        ),
        migrations.RemoveField(
            model_name='work',
            name='work_act',
        ),
        migrations.RemoveField(
            model_name='work',
            name='work_freq',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='worker_id',
        ),
        migrations.AddField(
            model_name='asset',
            name='assetid',
            field=models.CharField(default='foobar', max_length=25),
        ),
        migrations.AddField(
            model_name='work',
            name='task_act',
            field=models.CharField(default='foobar', max_length=25),
        ),
        migrations.AddField(
            model_name='work',
            name='task_freq',
            field=models.CharField(default='foobar', max_length=25),
        ),
        migrations.AddField(
            model_name='work',
            name='taskid',
            field=models.CharField(default='foobar', max_length=25),
        ),
        migrations.AddField(
            model_name='worker',
            name='workerid',
            field=models.CharField(default='foobar', max_length=25),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_name',
            field=models.CharField(default='foobar', max_length=25),
        ),
        migrations.AlterField(
            model_name='worker',
            name='worker_name',
            field=models.CharField(default='foobar', max_length=25),
        ),
    ]