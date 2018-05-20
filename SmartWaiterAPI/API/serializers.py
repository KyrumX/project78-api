#Default serializer for Menu
from rest_framework import serializers

from API.models import Menu, Order


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'type', 'price', 'allergy', 'description')

class MenuDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'type', 'price', 'allergy', 'description')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'tablenumber', 'datetime')

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'tablenumber', 'datetime')