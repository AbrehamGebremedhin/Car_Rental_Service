from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from accounts.models import Customer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

