from django.db import models

# Create your models here.


class DepartmentTable(models.Model):
    ddepartment = models.CharField(verbose_name="部门", max_length=40)
    dcetagory = models.CharField(verbose_name="类别",max_length=40)
    disdelte = models.BooleanField()

    def __str__(self):
        return self.ddepartment

    class Meta():
        verbose_name = "部门"
        verbose_name_plural = "部门字典"
