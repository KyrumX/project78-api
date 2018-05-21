#Default serializer for Menu
from rest_framework import serializers

from API.models import Menu, Order, OrderLine


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

class OrderLineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ('amount', 'menuitem_id')

class OrderDetailSerializer(serializers.ModelSerializer):
    lines = OrderLineDetailSerializer(source='orderlines_relation', many=True)

    class Meta:
        model = Order
        fields = ('id', 'tablenumber', 'datetime', 'lines')


