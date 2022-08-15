from rest_framework import serializers
from .models import Category, Product, Cart
from user.models import *
# from drf_extra_fields.fields import Base64ImageField
# from digits_operators_recognizer.resolver.models import Image
from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    farmer_name = serializers.CharField(source='farmer.username')
    # image = Base64ImageField()  # From DRF Extra Fields
    image = Base64ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = Product
        fields = '__all__'
        # read_only_fields = ('id', 'category_name', 'farmer_name')

    def validate(self, data):
        stock = data.get("stock")
        status = data.get("status")
        if stock > 0 and status == 0:
            raise serializers.ValidationError("product can't be out of stock while having stocks")
        elif stock == 0 and status == 1:
            raise serializers.ValidationError("product can't be in stock while don't having stocks")
        return data

    def create(self, validated_data):
        """
        create a product
        """
        product = Product.objects.create(**validated_data)
        product.save()
        return product

    # def update(self, instance, validated_data):
    #     instance.category = validated_data.get('category')
    #     instance.name = validated_data.get('name')
    #     instance.description = validated_data.get('description')
    #     instance.price = validated_data.get('price')
    #     instance.stock = validated_data.get('stock')
    #     if validated_data.get('status') == 'out of stock':
    #         instance.stock = 0
    #     else:
    #         instance.stock = 1
    #     instance.save()
    #     return instance


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

