# Generated by Django 2.0 on 2018-09-25 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=40, verbose_name='区域')),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '区域',
                'verbose_name_plural': '区域字典',
            },
        ),
        migrations.CreateModel(
            name='CategoryTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40, verbose_name='类别')),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别字典',
            },
        ),
        migrations.CreateModel(
            name='CompanyTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=40, verbose_name='公司')),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '公司',
                'verbose_name_plural': '公司字典',
            },
        ),
        migrations.CreateModel(
            name='DepartmentTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=40, verbose_name='部门')),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门字典',
            },
        ),
        migrations.CreateModel(
            name='EmployeeinfoTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(unique=True, verbose_name='工号')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('MM', '女性'), ('GG', '男性')], default=('MM', '女性'), max_length=50, verbose_name='性别')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('marita_status', models.CharField(blank=True, choices=[('married', '已婚'), ('unmarried', '未婚')], max_length=50, verbose_name='婚姻状态')),
                ('work_status', models.CharField(choices=[('on_the_job', '在职'), ('part_time_job', '兼职'), ('quit_job', '离职')], default=('on_the_job', '在职'), max_length=50, verbose_name='工作状态')),
                ('start_date', models.DateField(verbose_name='入职时间')),
                ('education', models.CharField(blank=True, choices=[('undergraduate', '本科'), ('specialty', '专科'), ('high_school', '高中')], max_length=50, null=True, verbose_name='学历')),
                ('graduate_school', models.CharField(blank=True, max_length=50, verbose_name='毕业院校')),
                ('graduation_date', models.DateField(blank=True, null=True, verbose_name='毕业日期')),
                ('start_work_date', models.DateField(blank=True, null=True, verbose_name='开始工作日期')),
                ('quit_date', models.DateField(blank=True, null=True, verbose_name='离职时间')),
                ('remarks', models.TextField(blank=True, max_length=1000, null=True, verbose_name='备注')),
                ('tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='联系电话')),
                ('emergency_contact_person', models.CharField(blank=True, max_length=50, null=True, verbose_name='紧急联系人')),
                ('emergency_contact_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='紧急联系电话')),
                ('isdelete', models.BooleanField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.AreaTable', verbose_name='区域')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.CategoryTable', verbose_name='部门类别')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.CompanyTable', verbose_name='公司')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.DepartmentTable', verbose_name='部门')),
            ],
            options={
                'verbose_name': '员工资料',
                'verbose_name_plural': '员工资料',
            },
        ),
        migrations.CreateModel(
            name='HouseholdRegisterTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('household_register', models.CharField(max_length=50, verbose_name='户籍')),
                ('isdelete', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': '户籍',
                'verbose_name_plural': '户籍字典',
            },
        ),
        migrations.CreateModel(
            name='NationTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nation', models.CharField(max_length=50, verbose_name='民族')),
                ('isdelete', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': '民族',
                'verbose_name_plural': '民族字典',
            },
        ),
        migrations.CreateModel(
            name='PositionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50, verbose_name='职位')),
                ('isdelete', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': '职位',
                'verbose_name_plural': '职位',
            },
        ),
        migrations.CreateModel(
            name='WorkLevelTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_level', models.CharField(max_length=50, verbose_name='工作级别')),
                ('isdelete', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': '工作级别',
                'verbose_name_plural': '工作级别',
            },
        ),
        migrations.AddField(
            model_name='employeeinfotable',
            name='household_register',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.HouseholdRegisterTable', verbose_name='户籍'),
        ),
        migrations.AddField(
            model_name='employeeinfotable',
            name='nation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.NationTable', verbose_name='民族'),
        ),
        migrations.AddField(
            model_name='employeeinfotable',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.PositionTable', verbose_name='职位'),
        ),
        migrations.AddField(
            model_name='employeeinfotable',
            name='work_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeinfo.WorkLevelTable', verbose_name='级别'),
        ),
    ]
