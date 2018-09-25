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

#3光纤网络表
class FiberAndNetworkTable(models.Model):
    fiber_number = models.CharField(verbose_name="光纤编号" , max_length=50)
    accounts = models.CharField(verbose_name="帐号", max_length=50)
    password = models.CharField(max_length=50, verbose_name="密码")
    ip_addr = models.GenericIPAddressField(verbose_name="ip地址")
    gateway = models.GenericIPAddressField(verbose_name="网关")
    subnet_mask = models.GenericIPAddressField(verbose_name="子网掩码")
    dns1 = models.GenericIPAddressField(verbose_name="主DNS")
    dns2 = models.GenericIPAddressField(verbose_name="次DNS")
    remarks = models.TextField(verbose_name="备注", max_length=1000)

    isdelete = models.BooleanField(default=0)
    bak1 = models.BooleanField(default=0)
    bak2 = models.BooleanField(default=0)
    bak3 = models.BooleanField(default=0)
    bak4 = models.BooleanField(default=0)

    supplier = models.ForeignKey(ContactsTable, verbose_name="联系人", on_delete=models.CASCADE)
    area = models.ForeignKey('employeeinfo.AreaTable', verbose_name="区域", on_delete=models.CASCADE)
    company = models.ForeignKey('employeeinfo.CompanyTable', verbose_name="公司", on_delete=models.CASCADE)


    def __str__(self):
        return self.fiber_number


    class Meta:
        verbose_name = "光纤网络"
        verbose_name_plural = verbose_name


#4软件资源库
class SoftResourceLibraryTable(models.Model):
    category = models.CharField(verbose_name="软件类型", max_length=50)
    sn = models.CharField(verbose_name="软件序号", max_length=50)
    guarantee = models.DateField(verbose_name="保修期")
    edition = models.CharField(verbose_name="软件版本", max_length=50)
    purchase_date = models.DateField(verbose_name="采购日期")
    remarks = models.TextField(verbose_name="备注", max_length=1000)

    isdelete = models.BooleanField(default=0)
    bak1 = models.BooleanField(default=0)
    bak2 = models.BooleanField(default=0)
    bak3 = models.BooleanField(default=0)
    bak4 = models.BooleanField(default=0)

    area = models.ForeignKey('employeeinfo.AreaTable', verbose_name="区域", on_delete=models.CASCADE)
    company = models.ForeignKey('employeeinfo.CompanyTable', verbose_name="公司", on_delete=models.CASCADE)
    department = models.ForeignKey('employeeinfo.DepartmentTable', verbose_name="部门", on_delete=models.CASCADE)



    def __str__(self):
        return self.category



    class Meta:
        verbose_name = "软件资源库"
        verbose_name_plural = verbose_name


#5硬件资源库
class HardwareResourceLibratyTable(models.Model):
    Fixed_assets_number = models.CharField(verbose_name="固定资产", max_length=50)
    brand = models.CharField(verbose_name="品牌", max_length=50)
    category = models.CharField(verbose_name="类型", max_length=50)
    model = models.CharField(verbose_name="型号", max_length=50)
    purchase_date = models.DateField(verbose_name="采购日期")
    guarantee =models.DateField(verbose_name="保修日期")
    service_code = models.CharField(verbose_name="服务代码", max_length=50)
    cpu = models.CharField(verbose_name="cpu", max_length=50)
    memory = models.CharField(verbose_name="内存", max_length=50)
    hard_disk = models.CharField(verbose_name="硬盘", max_length=50)
    remarks = models.TextField(verbose_name="备注", max_length=1000)
    area = models.ForeignKey('employeeinfo.AreaTable',verbose_name="区域", on_delete=models.CASCADE)
    company = models.ForeignKey('employeeinfo.CompanyTable', verbose_name="公司", on_delete=models.CASCADE)
    department = models.ForeignKey('employeeinfo.DepartmentTable', verbose_name="部门", on_delete=models.CASCADE)

    isdelete = models.BooleanField(default=0)
    bak1 = models.BooleanField(default=0)
    bak2 = models.BooleanField(default=0)
    bak3 = models.BooleanField(default=0)
    bak4 = models.BooleanField(default=0)

    def __str__(self):
        return self.Fixed_assets_number

    class Meta:
        verbose_name = "硬件资源库"
        verbose_name_plural = verbose_name


#6运维信息表
# class OperationinfoTable(models.Model):
#     area = models.ForeignKey('employeeinfo.AreaTable', verbose_name="区域", on_delete=models.CASCADE)
#     company = models.ForeignKey('employeeinfo.CompanyTable', verbose_name="公司", on_delete=models.CASCADE)
#     department = models.ForeignKey('employeeinfo.DepartmentTable', verbose_name="部门", on_delete=models.CASCADE)
#     name = models.ForeignKey('employeeinfo.EmployeeTable',)


#test表

class Bookinfo(models.Model):
    btitle = models.CharField("书名", max_length=50)
    binfo = models.CharField("描述", max_length=50)

    def __str__(self):
        return self.btitle



class Heroinfo(models.Model):
    name = models.CharField("姓名", max_length=50)
    gender = models.CharField("性别", max_length=50)
    hbook = models.ForeignKey(Bookinfo, verbose_name="书名", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "英雄"
        verbose_name_plural = verbose_name