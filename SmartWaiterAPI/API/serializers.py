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
    name = serializers.SerializerMethodField('get_item_name')

    def get_item_name(self, order_line):
        object = Menu.objects.get(id=order_line.id)
        name = object.name
        return name

    class Meta:
        model = OrderLine
        fields = ('amount', 'name', 'menuitem_id')

class OrderDetailSerializer(serializers.ModelSerializer):
    lines = OrderLineDetailSerializer(source='orderlines_relation', many=True)

    class Meta:
        model = Order
        fields = ('id', 'tablenumber', 'datetime', 'lines')


