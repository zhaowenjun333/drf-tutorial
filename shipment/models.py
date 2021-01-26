from django.conf import settings
from django.db import models

# Create your models here.
class ServiceCode(models.Model):
    name = models.CharField('渠道名称', max_length=20)
    code = models.CharField('渠道代码', max_length=20)

    class Meta:
        verbose_name = '下单代码列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Shipment(models.Model):
    number = models.CharField('订单号', max_length=50)
    service = models.ForeignKey(ServiceCode, verbose_name='渠道名称', on_delete=models.CASCADE)
    house_bill = models.ForeignKey('HouseBill', verbose_name='分单号', on_delete=models.SET_NULL, blank=True, null=True)
    create_time = models.DateTimeField('订单时间', auto_now_add=True)
    inputer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='操作人', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "订单列表"
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.number


class Package(models.Model):
    package_num = models.CharField('包裹号', max_length=50)
    shipment = models.ForeignKey(Shipment, verbose_name='订单号', on_delete=models.CASCADE)

    # 待补充包裹状态，寻物标签，溯源码等字段

    class Meta:
        verbose_name = '包裹列表'
        verbose_name_plural = verbose_name
        unique_together = ('package_num', 'shipment')

    def __str__(self):
        return self.package_num


class ShipmentCommodity(models.Model):
    package = models.ForeignKey(Package, verbose_name='包裹号', on_delete=models.CASCADE)
    sku = models.CharField('商品SKU', max_length=50)
    name_cn = models.CharField('中文品名', max_length=50)
    sku_value = models.DecimalField('价格', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = '商品列表'
        verbose_name_plural = verbose_name
        unique_together = ('package', 'sku')

    def __str__(self):
        return self.sku



class HouseBill(models.Model):
    number = models.CharField('分单号', max_length=50)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '分单列表'
        verbose_name_plural = '分单列表'

    def __str__(self):
        return self.number