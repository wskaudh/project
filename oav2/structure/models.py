from django.db import models

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
    Dcetagory = models.ForeignKey(CetagoryTable, verbose_name = "类别", on_delete=models.CASCADE,) #创建一个外健并做联动删除on_delete=models.CASCADE
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.Ddepartment

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门字典"


#架构表
class FrameTable(models.Model):
    Farea = models.ForeignKey(AreaTable, verbose_name="区域", on_delete=models.CASCADE,)
    Fcompany = models.ForeignKey(CompanyTable, verbose_name="公司", on_delete=models.CASCADE,)
    Fdepartment = models.ForeignKey(DepartmentTable, verbose_name="部门", on_delete=models.CASCADE,)
    isdelete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "构架体系"
        verbose_name_plural = "构架体系"






