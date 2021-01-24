import uuid as uuid
from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models

from bussinesspart.models import BussinessPart
from order.constant import OrderBussinessType, OrderStatus


class Order(models.Model):
    description=models.CharField(max_length=255,unique=True,help_text="描述",verbose_name="描述")
    bussiness_type=models.CharField(
        max_length=5,
        help_text="业务类型",
        verbose_name="业务类型",
        choices=OrderBussinessType.choices,
        default=OrderBussinessType.TAC,
    )
    status=models.IntegerField(
        max_length=2,
        help_text="订单状态",
        verbose_name="订单状态",
        choices=OrderStatus.choices,
        default=OrderStatus.CONFIRMED,
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid1().hex, editable=False)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    logistics_created_at=models.DateTimeField(verbose_name="物流时间")
    arrival_at=models.DateTimeField(verbose_name="订单到货时间")
    dealer=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="经销商",on_delete=models.DO_NOTHING)

    class Meta():
        db_table="dealer_orders"
        verbose_name="订单表"
        ordering=("created_at",)

    def __str__(self):
        ret={}
        ret.update(
            description=self.description,
            uuid=self.uuid
        )
        return self.description
class OrderItems(models.Model):
    class meta():
        db_table = "dealer_orders_items"
        ordering = ("price",)

    order= models.ForeignKey(Order,on_delete=models.DO_NOTHING,related_name="items")
    tyre = models.ForeignKey(BussinessPart,on_delete=models.DO_NOTHING )
    quantity = models.IntegerField(blank=False,null=False)
    price = models.FloatField( )

    def __str__(self):
        ret={}
        ret.update(
            order=self.order,
            quantity=self.quantity,
            price=self.price
        )
        return self.quantity.__str__()