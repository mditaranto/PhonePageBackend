from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Order, OrderSen

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderSenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSen
        fields = "__all__"