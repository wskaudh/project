#conding=utf-8
from django.db import models
# Create your models here.


#运维信息管理
#1供应商表
class SupplierTable(models.Model):
    area = models.ForeignKey('employeeinfo.AreaTable', verbose_name="区域", on_delete=models.CASCADE)
    supplier_name = models.CharField(verbose_name="供应商",  max_length=50)

    isdelete = models.BooleanField(default=0)

    def __str__(self):
        return self.supplier_name

    class Meta:
        verbose_name = "供应商"
        verbose_name_plural = verbose_name


#2联系人表
class ContactsTable(models.Model):
    contact_full_name = models.CharField(verbose_name="联系人", max_length=50)
    fixed_telephone = models.CharField(verbose_name="固定电话", blank=True, null=True,  max_length=50)
    phone_number = models.CharField(verbose_name="手机号码", blank=True, null=True, max_length=50)
    email = models.EmailField("Email")
    remarks = models.TextField("备注", max_length=1000, blank=True, null=True)

    isdelete = models.BooleanField(default=0)

    area = models.ForeignKey('employeeinfo.AreaTable', verbose_name="区域", on_delete=models.CASCADE)
    supplier_name = models.ForeignKey(SupplierTable, verbose_name="供应商", on_delete=models.CASCADE)

    def __str__(self):
        return self.contact_full_name

    class Meta:
        verbose_name = "联系人"
        verbose_name_plural = verbose_name
