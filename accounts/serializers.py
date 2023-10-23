from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from accounts.models import Customer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user', 'phone_number', 'driver_license']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        customer = Customer.objects.create(user=user, **validated_data)
        return customer
