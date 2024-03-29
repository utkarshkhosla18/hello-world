from product.models import *
from user.models import *


class CustomerOrder(models.Model):
    customer = models.ForeignKey('user.Customer', related_name='customer_orders', on_delete=models.CASCADE)
    pay_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'CustomerOrder'
        verbose_name = 'CustomerOrder'
        verbose_name_plural = verbose_name


class FarmerOrder(models.Model):
    farmer = models.ForeignKey('user.Farmer', related_name='farmer_orders', on_delete=models.CASCADE)
    CustomerOrderId = models.ForeignKey('CustomerOrder', related_name='c_order_farmer_orders', on_delete=models.CASCADE)
    pay_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'FarmerOrder'
        verbose_name = 'FarmerOrder'
        verbose_name_plural = verbose_name


class OrderItem(models.Model):
    CustomerOrderId = models.ForeignKey('CustomerOrder', related_name='customer_order_items', on_delete=models.CASCADE)
    ProductId = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'OrderItem'
        verbose_name = 'OrderItem'
        verbose_name_plural = verbose_name


# class OrderInfo(models.Model):
#     """
#     订单
#     """
#     ORDER_STATUS = (
#         ("TRADE_SUCCESS", "成功"),
#         ("TRADE_CLOSED", "超时关闭"),
#         ("WAIT_BUYER_PAY", "交易创建"),
#         ("TRADE_FINISHED", "交易结束"),
#         ("paying", "待支付"),
#     )
#
#     user = models.ForeignKey(User, verbose_name="用户")
#     order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号")
#     trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号")
#     pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="订单状态")
#     post_script = models.CharField(max_length=200, verbose_name="订单留言")
#     order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
#     pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
#
#     # 用户信息
#     address = models.CharField(max_length=100, default="", verbose_name="收货地址")
#     signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
#     singer_mobile = models.CharField(max_length=11, verbose_name="联系电话")
#
#     add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
#
#     class Meta:
#         verbose_name = u"订单"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.order_sn)
#
# class OrderGoods(models.Model):
#     """
#     订单的商品详情
#     """
#     order = models.ForeignKey(OrderInfo, verbose_name="订单信息", related_name="goods")
#     goods = models.ForeignKey(Goods, verbose_name="商品")
#     goods_num = models.IntegerField(default=0, verbose_name="商品数量")
#
#     add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
#
#     class Meta:
#         verbose_name = "订单商品"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.order.order_sn)