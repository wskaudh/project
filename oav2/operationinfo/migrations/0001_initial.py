# Generated by Django 2.0 on 2018-09-20 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employeeinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_full_name', models.CharField(max_length=50, verbose_name='联系人')),
                ('fixed_telephone', models.IntegerField(blank=True, null=True, verbose_name='固定电话')),
                ('phone_number', models.IntegerField(blank=True, null=True, verbose_name='手机号码')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('remarks', models.TextField(blank=True, max_length=1000, null=True, verbose_name='备注')),
                ('isdelete', models.BooleanField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.AreaTable', verbose_name='区域')),
            ],
            options={
                'verbose_name': '联系人',
                'verbose_name_plural': '联系人',
            },
        ),
        migrations.CreateModel(
            name='SupplierTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=50, verbose_name='供应商')),
                ('isdelete', models.BooleanField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.AreaTable', verbose_name='区域')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
            },
        ),
        migrations.AddField(
            model_name='contactstable',
            name='supplier_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operationinfo.SupplierTable', verbose_name='供应商'),
        ),
    ]