from rest_framework import serializers
from .models import Farmer, Customer, Admin
from .models import Address
from django.core.mail import send_mail
from itsdangerous import TimedJSONWebSignatureSerializer as TJWSS
from backend import settings


class FarmerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    date_joined = serializers.DateTimeField(read_only=True)
    email_active = serializers.BooleanField(default=False)
    usertype = serializers.CharField(max_length=128, default='farmer')
    mobile = serializers.CharField(max_length=11, default='')
    # first_name = serializers.CharField(max_length=150, allow_null=True, allow_blank=True)
    # last_name = serializers.CharField(max_length=150, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        """
        create a farmer
        """
        farmer = Farmer.objects.create(**validated_data)
        farmer.set_password(validated_data['password'])
        farmer.save()
        return farmer

    def update(self, instance, validated_data):
        """update profile"""
        # user = super().create(validated_data)
        instance.username = validated_data.get('username')
        instance.set_password(validated_data['password'])
        instance.email = validated_data.get('email')
        # instance.first_name = validated_data.get('first_name')
        # instance.last_name = validated_data.get('last_name')
        instance.mobile = validated_data.get('mobile')
        # save the update
        instance.save()

        return instance


class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    date_joined = serializers.DateTimeField(read_only=True)
    email_active = serializers.BooleanField(default=False)
    usertype = serializers.CharField(max_length=128, default='customer')
    # mobile = serializers.CharField(max_length=11)
    # first_name = serializers.CharField(max_length=150, allow_blank=True)
    # last_name = serializers.CharField(max_length=150, allow_blank=True)

    def create(self, validated_data):
        """
        create customer
        """
        customer = Customer.objects.create(**validated_data)
        customer.set_password(validated_data['password'])
        customer.save()
        return customer

    def update(self, instance, validated_data):
        """update profile"""
        instance.username = validated_data.get('username')
        instance.set_password(validated_data['password'])
        instance.email = validated_data.get('email')
        # instance.first_name = validated_data.get('first_name')
        # instance.last_name = validated_data.get('last_name')
        # instance.mobile = validated_data.get('mobile')
        # save the update
        instance.save()

        return instance


class AdminSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    email_active = serializers.BooleanField(default=False)
    usertype = serializers.CharField(max_length=128, default='admin')
    # mobile = serializers.CharField(max_length=11)
    # first_name = serializers.CharField(max_length=150, allow_blank=True)
    # last_name = serializers.CharField(max_length=150, allow_blank=True)

    def create(self, validated_data):
        """
        create customer
        """
        admin = Admin.objects.create(**validated_data)
        admin.set_password(validated_data['password'])
        admin.save()
        return admin

    def update(self, instance, validated_data):
        """update profile"""
        instance.username = validated_data.get('username')
        instance.set_password(validated_data['password'])
        instance.email = validated_data.get('email')
        # instance.first_name = validated_data.get('first_name')
        # instance.last_name = validated_data.get('last_name')
        # instance.mobile = validated_data.get('mobile')
        # save the update
        instance.save()

        return instance


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


    # from_email = settings.DEFAULT_FROM_EMAIL
    # url = 'http://127.0.0.1:8000/users/email_verify/'+'token'+'/'
    # html_msg = '<a href=' + url + '>激活链接地址</a>'
    # # 可以用html_message然后加个a标签确认可以点击
    # # 必填四个参数，1是邮件主题，2是邮件信息，可以为空用html_message代替
    #     # 3是发件人，4是收件人，类型为一个列表
    # send_mail('用户邮件激活', '点击链接激活邮箱:'+ url, from_email, ['xiongfeibaba@gmail.com', ], html_message='点击这个激活:'+html_msg)

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'email')

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        '''
        :param instance: 视图传递过来的实例对象，get_object获取的
        :param validated_data: 校验完的数据
        :return:
        '''
        print('1111111111111111111111111')
        print(validated_data)
        instance.email = validated_data['email']
        instance.save()
        # 生成激活链接
        # # tjwss = TJWSS(秘钥, 有效期(单位秒)) 不写的话默认时间为3600秒
        # Django项目中setting中自带了一个秘钥直接使用,其他地方 可以先生成一个秘钥,再使用
        tjwss = TJWSS(settings.SECRET_KEY, 60 * 60)

        # 要加密的数据
        data = {
            'id': instance.id,
            "email": instance.email,
        }
        # 加密 tjwss.dumps(数据), 返回bytes类型
        token = tjwss.dumps(data).decode()

        # 发送邮件
        from_email = settings.DEFAULT_FROM_EMAIL
        url = 'http://127.0.0.1:8000/farmer/email_verify/' + token + '/'
        html_msg = '<a href=' + url + '>激活链接地址</a>'
        # 可以用html_message然后加个a标签确认可以点击
        # 必填四个参数，1是邮件主题，2是邮件信息，可以为空用html_message代替
        # 3是发件人，4是收件人，类型为一个列表
        send_mail('用户邮件激活', '点击链接激活邮箱:' + url, from_email, ['paul0926@foxmail.com', ],
                  html_message='点击这个激活:' + html_msg)
        return instance


class EmailVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ('id', 'email', 'email_active')

    def update(self, instance, validated_data):
        instance.id = validated_data['id']
        instance.email = validated_data['email']
        instance.email_active = validated_data['email_active']
        return instance
