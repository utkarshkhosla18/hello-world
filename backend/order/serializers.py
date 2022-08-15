
from rest_framework import serializers
from .models import *
from user.models import *
from product.models import *


class FarmerOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmerOrder
        fields = '__all__'


class CustomerOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerOrder
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     category_name = serializers.CharField(source='category.name')
#     farmer_name = serializers.CharField(source='farmer.username')
#     # image = Base64ImageField()  # From DRF Extra Fields
#     image = Base64ImageField(
#         max_length=None, use_url=True
#     )
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#         # read_only_fields = ('id', 'category_name', 'farmer_name')
#
#     def validate(self, data):
#         stock = data.get("stock")
#         status = data.get("status")
#         if stock > 0 and status == 0:
#             raise serializers.ValidationError("product can't be out of stock while having stocks")
#         elif stock == 0 and status == 1:
#             raise serializers.ValidationError("product can't be in stock while don't having stocks")
#         return data
#
#     def create(self, validated_data):
#         """
#         create a product
#         """
#         product = Product.objects.create(**validated_data)
#         product.save()
#         return product
#
#     # def update(self, instance, validated_data):
#     #     instance.category = validated_data.get('category')
#     #     instance.name = validated_data.get('name')
#     #     instance.description = validated_data.get('description')
#     #     instance.price = validated_data.get('price')
#     #     instance.stock = validated_data.get('stock')
#     #     if validated_data.get('status') == 'out of stock':
#     #         instance.stock = 0
#     #     else:
#     #         instance.stock = 1
#     #     instance.save()
#     #     return instance
#
#
# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = '__all__'

