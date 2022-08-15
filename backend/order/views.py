from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from user.models import *
from product.models import *
from .serializers import *



class CustomerOrderView(APIView):
    """
    get, create order for the customer
    """
    def get(self, request, customer_pk, format=None):
        customer = Customer.objects.get(pk=customer_pk)
        order_list = customer.customer_orders
        serializer = CustomerOrderSerializer(order_list, many=True)
        return Response(serializer.data)

    def post(self, request, customer_pk, format=None):
        data = request.data
        total_price = 0
        for key in data:
            data_instance = data[key]
            product = Product.objects.get(pk=data_instance['product'])
            total_price += product.price * data_instance['quantity']
        c_order_serializer = CustomerOrderSerializer(data={
            'customer': customer_pk,
            'total_price': total_price
        })
        if c_order_serializer.is_valid():
            c_order_serializer.save()
            # print(c_order_serializer.data.get('id'))

        farmer_order_dict = {}
        for key in data:
            data_instance = data[key]
            product = Product.objects.get(pk=data_instance['product'])
            farmer_id = product.farmer_id
            if farmer_id in farmer_order_dict.keys():
                farmer_order_dict[farmer_id] += product.price * data_instance['quantity']
            else:
                farmer_order_dict[farmer_id] = product.price * data_instance['quantity']
            # cart = Cart.objects.filter(product=product.id, customer=customer_pk)
            serializer = OrderItemSerializer(data={
                'ProductId': product.id,
                'quantity': data_instance['quantity'],
                'CustomerOrderId': c_order_serializer.data.get('id'),
                'total_price': product.price * data_instance['quantity']
            })
            if serializer.is_valid():
                serializer.save()

        for key in farmer_order_dict:
            serializer = FarmerOrderSerializer(data={
                'farmer': key,
                'total_price': farmer_order_dict[key],
                'CustomerOrderId': c_order_serializer.data.get('id')
            })
            if serializer.is_valid():
                serializer.save()

        return Response({'create order success'}, status=status.HTTP_201_CREATED)


class FarmerOrderView(APIView):
    """
    get order for the farmer
    """
    def get(self, request, farmer_pk, format=None):
        farmer = Farmer.objects.get(pk=farmer_pk)
        order_list = farmer.farmer_orders
        serializer = FarmerOrderSerializer(order_list, many=True)
        return Response(serializer.data)


class ALLFarmerOrderView(APIView):
    """
    get all farmer's orders
    """
    def get(self, request, format=None):
        order_list = FarmerOrder.objects.all()
        # order_list = farmer.farmer_orders
        serializer = FarmerOrderSerializer(order_list, many=True)
        return Response(serializer.data)


class ALLCustomerOrderView(APIView):
    """
    get all customer's orders
    """
    def get(self, request, format=None):
        order_list = CustomerOrder.objects.all()
        # order_list = farmer.farmer_orders
        serializer = CustomerOrderSerializer(order_list, many=True)
        return Response(serializer.data)

