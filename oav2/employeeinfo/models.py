#coding=utf-8
from django.db import models

# Create your models here.


#员工信息表
class EmployeeinfoTable(models.Model):
    Eemployee_id = models.IntegerField(verbose_name="工号", max_length=6)
    Ename = models.CharField(verbose_name="姓名", max_length=40)
    Egender = models.CharField(verbose_name="性别", max_length=4)
    Eage = models.IntegerField(verbose_name="年龄", max_length=4)
    Emarita_status = models.CharField(verbose_name="婚姻状态", max_length=8)
    Ework_status = models.CharField(verbose_name="工作状态", max_length=8)
    Estart_date = models.DateField(verbose_name="入职时间")
    Eposition = models.CharField(verbose_name="职位", max_length=10)
    Ework_level = models.CharField(verbose_name="级别", max_length=10)
    Eeducation = models.CharField(verbose_name="学历", max_length=8)
    Egraduate_school = models.CharField(verbose_name="毕业院校", max_length=40)
    Egraduation_date = models.DateField(verbose_name="毕业日期")
    Estart_work_date = models.DateField(verbose_name="开始工作日期")
    Ehousehold_register = models.CharField(verbose_name="户籍", max_length=20)
    Enation = models.CharField(verbose_name="民族", max_length=20)
    Equit_date =models.DateField(verbose_name="离职时间")
    Eremarks = models.TextField(verbose_name="备注", max_length=1000)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.Ename

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = "员工信息"