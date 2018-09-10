#coding=utf-8
from django.db import models
from structure import *

# Create your models here.

#类别表
class CetagoryTable(models.Model):
    Ccetagory = models.CharField(verbose_name="类别", max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.Ccetagory

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = "类别字典"

#区域表
class AreaTable(models.Model):
    Aarea = models.CharField(verbose_name="区域",max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.Aarea

    class Meta:
        verbose_name = "区域"
        verbose_name_plural = "区域字典"

#公司表
class CompanyTable(models.Model):
    Ccompany = models.CharField(verbose_name="公司", max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.Ccompany

    class Meta:
        verbose_name = "公司"
        verbose_name_plural = "公司字典"

#部门表
class DepartmentTable(models.Model):
    Ddepartment = models.CharField(verbose_name="部门", max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.Ddepartment

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门字典"


#职位表
class PositionTable(models.Model):
    pposition = models.CharField(verbose_name="职位", max_length=50)
    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.pposition

    class Meta:
        verbose_name = "职位"
        verbose_name_plural = verbose_name

#工作级别表
class WorkLevelTable(models.Model):
    wwork_level = models.CharField(verbose_name="工作级别", max_length=50)
    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.wwork_level

    class Meta:
        verbose_name = "工作级别"
        verbose_name_plural = verbose_name


#民族表
class NationTable(models.Model):
    nnation = models.CharField(verbose_name="民族", max_length=50)
    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.nnation

    class Meta:
        verbose_name = "民族"
        verbose_name_plural = "民族字典"

#户籍表
class HouseholdRegisterTable(models.Model):
    hhousehold_register = models.CharField(verbose_name="户籍", max_length=50)
    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.hhousehold_register

    class Meta:
        verbose_name = "户籍"
        verbose_name_plural = "户籍字典"


#员工信息表
class EmployeeinfoTable(models.Model):
    Eemployee_id = models.IntegerField(verbose_name="工号", unique=True)
    Ename = models.CharField(verbose_name="姓名", max_length=50, unique=True)

    gender_choices = (   #choice属性
        ('MM', '女性'),
        ('GG', '男性')
    )
    Egender = models.CharField(verbose_name="性别", choices=gender_choices,default=gender_choices[0], max_length=50) #设置choice属性 并且默认为True即是女性
    Eage = models.IntegerField(verbose_name="年龄", blank=True, null=True)

    marrita_status_choices = (   #choice属性
        ('married', '已婚'),
        ('unmarried', '未婚')
    )
    Emarita_status = models.CharField(verbose_name="婚姻状态", max_length=50, blank=True, choices=marrita_status_choices)

    work_status_choices = ( #choice属性
        ('on_the_job', '在职'),
        ('part_time_job', '兼职'),
        ('quit_job', '离职')
    )
    Ework_status = models.CharField(verbose_name="工作状态", max_length=50, choices=work_status_choices, default=work_status_choices[0])
    Estart_date = models.DateField(verbose_name="入职时间")

    education_choices = (  # choice属性
        ('undergraduate', '本科'),
        ('specialty', '专科'),
        ('high school', '高中')
    )
    Eeducation = models.CharField(verbose_name="学历", max_length=50, blank=True, choices=education_choices)
    Egraduate_school = models.CharField(verbose_name="毕业院校", max_length=50,blank=True)
    Egraduation_date = models.DateField(verbose_name="毕业日期" ,blank=True, null=True)
    Estart_work_date = models.DateField(verbose_name="开始工作日期" ,blank=True, null=True)
    Equit_date =models.DateField(verbose_name="离职时间", blank=True, null=True)
    Eremarks = models.TextField(verbose_name="备注", max_length=1000, blank=True, null=True)
    Etel = models.CharField(verbose_name="联系电话", max_length=50, blank=True, null=True)
    Eemergency_contact_person = models.CharField(verbose_name="紧急联系人", max_length=50 ,blank=True, null=True)
    Eemergency_contact_number = models.CharField(verbose_name="紧急联系电话", max_length=50 ,blank=True, null=True)


    isdelete = models.BooleanField(default=0)

    #外健写在最下面
    Eposition = models.ForeignKey(PositionTable, verbose_name="职位", on_delete=models.CASCADE)
    Ework_level = models.ForeignKey(WorkLevelTable, verbose_name="级别", on_delete=models.CASCADE)
    Earea = models.ForeignKey(AreaTable, verbose_name="区域", on_delete=models.CASCADE)
    Ecompany = models.ForeignKey(CompanyTable, verbose_name="公司", on_delete=models.CASCADE)
    Edepartment = models.ForeignKey(DepartmentTable, verbose_name="部门", on_delete=models.CASCADE)
    Ecetagory = models.ForeignKey(CetagoryTable, verbose_name="部门类别", on_delete=models.CASCADE)
    Enation = models.ForeignKey(NationTable, verbose_name="民族",blank=True, null=True, on_delete=models.CASCADE)
    Ehousehold_register = models.ForeignKey(HouseholdRegisterTable, verbose_name="户籍", blank=True, null=True, on_delete=models.CASCADE)



    def __str__(self):
        return self.Ename

    class Meta:
        verbose_name = "员工资料"
        verbose_name_plural = verbose_name