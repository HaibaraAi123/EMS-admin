# Generated by Django 2.2.6 on 2020-07-23 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EMSLogConfig',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('log_addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('log_type', models.CharField(max_length=20, verbose_name='日志类型')),
                ('log_content', models.CharField(max_length=255, verbose_name='内容')),
                ('log_user', models.CharField(max_length=255, verbose_name='操作人')),
                ('log_ip', models.CharField(max_length=255, verbose_name='操作IP')),
            ],
            options={
                'permissions': (('users_syslog', '日志管理'),),
            },
        ),
    ]
