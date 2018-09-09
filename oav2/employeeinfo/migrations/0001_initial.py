# Generated by Django 2.0 on 2018-09-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeinfoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Eemployee_id', models.IntegerField(max_length=6, verbose_name='工号')),
                ('Ename', models.CharField(max_length=40, verbose_name='姓名')),
                ('Egender', models.CharField(max_length=4, verbose_name='性别')),
                ('Eage', models.IntegerField(max_length=4, verbose_name='年龄')),
                ('Emarita_status', models.CharField(max_length=8, verbose_name='婚姻状态')),
                ('Ework_status', models.CharField(max_length=8, verbose_name='工作状态')),
                ('Estart_date', models.DateField(verbose_name='入职时间')),
                ('Eposition', models.CharField(max_length=10, verbose_name='职位')),
                ('Ework_level', models.CharField(max_length=10, verbose_name='级别')),
                ('Eeducation', models.CharField(max_length=8, verbose_name='学历')),
                ('Egraduate_school', models.CharField(max_length=40, verbose_name='毕业院校')),
                ('Egraduation_date', models.DateField(verbose_name='毕业日期')),
                ('Estart_work_date', models.DateField(verbose_name='开始工作日期')),
                ('Ehousehold_register', models.CharField(max_length=20, verbose_name='户籍')),
                ('Enation', models.CharField(max_length=20, verbose_name='民族')),
                ('Equit_date', models.DateField(verbose_name='离职时间')),
                ('Eremarks', models.TextField(max_length=1000, verbose_name='备注')),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '员工信息',
                'verbose_name_plural': '员工信息',
            },
        ),
    ]