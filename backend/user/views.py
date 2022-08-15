import json

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.http import Http404

from .models import Farmer, Customer, Address, Admin
# from .models import FarmerToken, CustomerToken,  AdminToken
from .serializers import FarmerSerializer, CustomerSerializer, AddressSerializer, EmailSerializer, EmailVerifySerializer
from .serializers import AdminSerializer
from itsdangerous import TimedJSONWebSignatureSerializer as TJWSS
from backend import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class Register(APIView):
    """
    register for different usertype
    """
    def post(self, request, format=None):
        data = request.data
        if data['usertype'] == 'farmer':
            farmer = Farmer.objects.filter(email=data['email'])
            if farmer.exists():
                info = {'info': 'this email has been registered'}
                return Response(info, status= status.HTTP_400_BAD_REQUEST)
            else:
                serializer = FarmerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif data['usertype'] == 'customer':
            customer = Customer.objects.filter(email=data['email'])
            if customer.exists():
                info = {'info': 'this email has been registered'}
                return Response(info, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = CustomerSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif data['usertype'] == 'admin':
            admin = Admin.objects.filter(email=data['email'])
            if admin.exists():
                info = {'info': 'this email has been registered'}
                return Response(info, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = AdminSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FarmerList(APIView):
    """
    list all farmers
    """
    def get(self, request, format=None):
        farmers = Farmer.objects.all()
        serializer = FarmerSerializer(farmers, many=True)
        return Response(serializer.data)


class FarmerDetail(APIView):
    """
    Retrieve, update or delete a farmer instance
    """
    def get_object(self, pk):
        try:
            return Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        farmer = self.get_object(pk)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        farmer = self.get_object(pk)
        serializer = FarmerSerializer(instance=farmer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        farmer = self.get_object(pk)
        farmer.delete()
        info = {'info': 'delete success'}
        return Response(info, status=status.HTTP_204_NO_CONTENT)


class CustomerList(APIView):
    """
    list all customers
    """
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


class CustomerDetail(APIView):
    """
    Retrieve, update or delete a customer instance
    """
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        info = {'info': 'delete success'}
        return Response(info, status=status.HTTP_204_NO_CONTENT)


class AdminList(APIView):
    """
    list all customers
    """
    def get(self, request, format=None):
        customers = Admin.objects.all()
        serializer = AdminSerializer(customers, many=True)
        return Response(serializer.data)


class AdminDetail(APIView):
    """
    Retrieve, update or delete a customer instance
    """
    def get_object(self, pk):
        try:
            return Admin.objects.get(pk=pk)
        except Admin.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        admin = self.get_object(pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        admin = self.get_object(pk)
        serializer = AdminSerializer(instance=admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        admin = self.get_object(pk)
        admin.delete()
        info = {'info': 'delete success'}
        return Response(info, status=status.HTTP_204_NO_CONTENT)


class AddressList(APIView):
    """
    list all address or create an address
    """
    def get(self, request, format=None):
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # user_data = JSONParser().parse(request)
        # serializer = CustomerSerializer(data=user_data)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddressDetail(APIView):
    """
    Retrieve, update or delete an address instance
    """
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        address = self.get_object(pk)
        serializer = AddressSerializer(instance=address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        address = self.get_object(pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddressForCustomer(APIView):
    """
    Retrieve, update or delete an address instance for the customer
    """
    def get_object(self, customer_pk):
        try:
            return Address.objects.get(customer_id=customer_pk)
        except Address.DoesNotExist:
            raise Http404

    def post(self, request, customer_pk, format=None):
        # user_data = JSONParser().parse(request)
        # serializer = CustomerSerializer(data=user_data)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, customer_pk, format=None):
        address_queryset = Address.objects.filter(customer_id=customer_pk)
        if address_queryset.exists():
            address = self.get_object(customer_pk)
            serializer = AddressSerializer(address)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            info = {'info': 'address not exist, please add address first'}
            return Response(info, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, customer_pk, format=None):
        address = self.get_object(customer_pk)
        serializer = AddressSerializer(instance=address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_pk, format=None):
        address = self.get_object(customer_pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Login(APIView):
    """
    Login authentication
    """
    def post(self, request, format=None):
        data = request.data
        email = data['email']
        pwd = data['password']
        usertype = data['usertype']
        if not all([email, pwd, usertype]):
            return Response({'info': 'information incomplete', 'code': 400})
        if usertype == 'farmer':
            # usertype = 'farmer'
            farmer_queryset = Farmer.objects.filter(email=email)
            if farmer_queryset.exists():
                farmer = Farmer.objects.get(email=email)
                if not farmer.email_active:
                    return send_email(farmer, usertype)
                else:
                    return check_password(farmer, usertype, pwd)
            else:
                res = {'info': 'please register first', 'code': 401}
                return Response(res)
        elif usertype == 'customer':
            # usertype = 'customer'
            customer_queryset = Customer.objects.filter(email=email)
            if customer_queryset.exists():
                customer = Customer.objects.get(email=email)
                if not customer.email_active:
                    return send_email(customer, usertype)
                else:
                    return check_password(customer, usertype, pwd)
            else:
                res = {'info': 'please register first', 'code': 401}
                return Response(res)
        elif usertype == 'admin':
            # usertype = 'admin'
            customer_queryset = Customer.objects.filter(email=email)
            if customer_queryset.exists():
                admin = Admin.objects.get(email=email)
                if not admin.email_active:
                    return send_email(admin, usertype)
                else:
                    return check_password(admin, usertype, pwd)
            else:
                res = {'info': 'please register first', 'code': 401}
                return Response(res)


def send_email(user, usertype):
    tjwss = TJWSS(settings.SECRET_KEY, 60 * 60)
    # data to encode
    data = {
        'id': user.id,
        "email": user.email,
    }
    # encode tjwss.dumps(data), return bytes type
    token = tjwss.dumps(data).decode()

    # 发送邮件
    from_email = settings.DEFAULT_FROM_EMAIL
    url = 'http://127.0.0.1:8000/api/'+usertype+'/email_verify/' + token
    html_msg = '<a href=' + url + '>激活链接地址</a>'
    # You can use html_message and then add a tag to confirm that you can click
    # Four parameters are required, 1 is the subject of the email,
    # and 2 is the email information, which can be empty and replaced by html_message
    # 3 is the sender, 4 is the recipient, type is a list
    send_mail(usertype + ' email verify', 'Click the link to activate:' + url, from_email, [user.email])
    return Response({'info': 'validation email has been sent', 'code': 401})


def check_password(user, usertype, pwd):
    if user.check_pwd(pwd):
        if usertype == 'farmer':
            serializer = FarmerSerializer(user)
        elif usertype == 'customer':
            serializer = CustomerSerializer(user)
        elif usertype == 'admin':
            serializer = AdminSerializer(user)
        # response_data = {'data': serializer.data, 'usertype': usertype}
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        res = {'info': usertype + 'wrong password', 'code': 401}
        return Response(res)


class FarmerEmailVerifyView(APIView):
    """
    activate email
    """
    def get(self, request, token):
        # Decrypt with the method of itsdangerou module
        ts_obj = TJWSS(settings.SECRET_KEY, 60 * 30)
        user_obj = ts_obj.loads(token)
        # get user by id value
        user = Farmer.objects.get(id=user_obj['id'])
        # Set the active state to 1, save
        user.email_active = True
        user.save()
        res = 'Verification succeeded, please login again'
        return Response(res, status=status.HTTP_200_OK)


class CustomerEmailVerifyView(APIView):
    """
    activate email
    """
    def get(self, request, token):
        # Decrypt with the method of itsdangerou module
        ts_obj = TJWSS(settings.SECRET_KEY, 60 * 30)
        user_obj = ts_obj.loads(token)
        # get user by id value
        user = Customer.objects.get(id=user_obj['id'])
        # Set the active state to 1, save
        user.email_active = True
        user.save()
        res = 'Verification succeeded, please login again'
        return Response(res, status=status.HTTP_200_OK)


class AdminEmailVerifyView(APIView):
    """
    activate email
    """
    def get(self, request, token):
        # Decrypt with the method of itsdangerou module
        ts_obj = TJWSS(settings.SECRET_KEY, 60 * 30)
        user_obj = ts_obj.loads(token)
        # get user by id value
        user = Admin.objects.get(id=user_obj['id'])
        # Set the active state to 1, save
        user.email_active = True
        user.save()
        res = 'Verification succeeded, please login again'
        return Response(res, status=status.HTTP_200_OK)

