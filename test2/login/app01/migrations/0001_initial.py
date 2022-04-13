# Generated by Django 3.2.5 on 2022-04-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('pwd', models.CharField(max_length=32, verbose_name='密码')),
            ],
            options={
                'verbose_name_plural': '用户',
            },
        ),
    ]
