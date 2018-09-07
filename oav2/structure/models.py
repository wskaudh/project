from django.db import models

# Create your models here.

class CetagoryTable(models.Model):
    ccetagory = models.CharField(verbose_name="类别", max_length=40)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ccetagory

    class Meta():
        verbose_name = "类别"
        verbose_name_plural = "类别字典"


class DepartmentTable(models.Model):
    ddepartment = models.CharField(verbose_name="部门", max_length=40)
    dcetagory = models.ForeignKey(CetagoryTable, verbose_name = "类别", on_delete=models.CASCADE,) #创建一个外健并做联动删除on_delete=models.CASCADE
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ddepartment

    class Meta():
        verbose_name = "部门"
        verbose_name_plural = "部门字典"






