import uuid as uuid

from django.conf import settings
from django.db import models

# Create your models here.

class BussinessPart(models.Model):
    class meta():
        db_table = "bussiness_part"
    description=models.CharField(max_length=255,unique=True,help_text="描述",verbose_name="描述")
    name=models.CharField(max_length=64,verbose_name="商品名称")
    uuid = models.TextField(primary_key=True, default=uuid.uuid1().hex, editable=False)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    mbpn = models.TextField( max_length=128,   unique=True,db_index=True ,blank=False,null=False)

    def __str__(self):
        ret={}
        ret.update(
            name=self.name,
            mbpn=self.mbpn
        )
        return self.name