#coding=utf-8
from django.db import models


# Create your models here.

#类别表
class CategoryTable(models.Model):
    category = models.CharField(verbose_name="类别", max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别字典"

#区域表
class AreaTable(models.Model):
    area = models.CharField(verbose_name="区域",max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = "区域"
        verbose_name_plural = "区域字典"

#公司表
class CompanyTable(models.Model):
    company = models.CharField(verbose_name="公司", max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "公司"
        verbose_name_plural = "公司字典"

#部门表
class DepartmentTable(models.Model):
    department = models.CharField(verbose_name="部门", max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门字典"


#职位表
class PositionTable(models.Model):
    position = models.CharField(verbose_name="职位", max_length=50)
    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = "职位"
        verbose_name_plural = verbose_name

#工作级别表
class WorkLevelTable(models.Model):
    work_level = models.CharField(verbose_name="工作级别", max_length=50)
    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.work_level

    class Meta:
        verbose_name = "工作级别"
        verbose_name_plural = verbose_name


#民族表
class NationTable(models.Model):
    nation = models.CharField(verbose_name="民族", max_length=50)
    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.nation

    class Meta:
        verbose_name = "民族"
        verbose_name_plural = "民族字典"

#户籍表
class HouseholdRegisterTable(models.Model):
    household_register = models.CharField(verbose_name="户籍", max_length=50)
    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.household_register

    class Meta:
        verbose_name = "户籍"
        verbose_name_plural = "户籍字典"


#员工信息表
class EmployeeinfoTable(models.Model):
    employee_id = models.IntegerField(verbose_name="工号", unique=True)
    name = models.CharField(verbose_name="姓名", max_length=50, unique=True)

    gender_choices = (   #choice属性
        ('MM', '女性'),
        ('GG', '男性')
    )
    gender = models.CharField(verbose_name="性别", choices=gender_choices,default=gender_choices[0], max_length=50) #设置choice属性 并且默认为True即是女性
    age = models.IntegerField(verbose_name="年龄", blank=True, null=True)

    marita_status_choices = (   #choice属性
        ('married', '已婚'),
        ('unmarried', '未婚')
    )
    marita_status = models.CharField(verbose_name="婚姻状态", max_length=50, blank=True, choices=marita_status_choices)

    work_status_choices = ( #choice属性
        ('on_the_job', '在职'),
        ('part_time_job', '兼职'),
        ('quit_job', '离职')
    )
    work_status = models.CharField(verbose_name="工作状态", max_length=50, choices=work_status_choices, default=work_status_choices[0])
    start_date = models.DateField(verbose_name="入职时间")

    education_choices = (  # choice属性
        ('undergraduate', '本科'),
        ('specialty', '专科'),
        ('high_school', '高中')
    )
    education = models.CharField(verbose_name="学历", max_length=50, blank=True, null=True, choices=education_choices)
    graduate_school = models.CharField(verbose_name="毕业院校", max_length=50,blank=True)
    graduation_date = models.DateField(verbose_name="毕业日期" ,blank=True, null=True)
    start_work_date = models.DateField(verbose_name="开始工作日期" ,blank=True, null=True)
    quit_date =models.DateField(verbose_name="离职时间", blank=True, null=True)
    remarks = models.TextField(verbose_name="备注", max_length=1000, blank=True, null=True)
    tel = models.CharField(verbose_name="联系电话", max_length=50, blank=True, null=True)
    emergency_contact_person = models.CharField(verbose_name="紧急联系人", max_length=50 ,blank=True, null=True)
    emergency_contact_number = models.CharField(verbose_name="紧急联系电话", max_length=50 ,blank=True, null=True)


    isdelete = models.BooleanField(default=0)

    #外健写在最下面
    position = models.ForeignKey(PositionTable, verbose_name="职位", on_delete=models.CASCADE)
    work_level = models.ForeignKey(WorkLevelTable, verbose_name="级别", on_delete=models.CASCADE)
    area = models.ForeignKey(AreaTable, verbose_name="区域", on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyTable, verbose_name="公司", on_delete=models.CASCADE)
    department = models.ForeignKey(DepartmentTable, verbose_name="部门", on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryTable, verbose_name="部门类别", on_delete=models.CASCADE)
    nation = models.ForeignKey(NationTable, verbose_name="民族",blank=True, null=True, on_delete=models.CASCADE)
    household_register = models.ForeignKey(HouseholdRegisterTable, verbose_name="户籍", blank=True, null=True, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "员工资料"
        verbose_name_plural = verbose_name