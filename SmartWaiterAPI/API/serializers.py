#Default serializer for Menu
from rest_framework import serializers

from API.models import Menu, Order, OrderLine, GoesWellWith


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

class OrderLineDetailCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ('amount', 'menuitem', 'orderid')

    def create(self, validated_data):
        if OrderLine.objects.filter(menuitem=validated_data['menuitem'], orderid=validated_data['orderid']).exists():
            print("UPDATING!")
            object = OrderLine.objects.get(menuitem=validated_data['menuitem'], orderid=validated_data['orderid'])
            object.amount = object.amount + validated_data['amount']
            object.save()
            return object
        else:
            print("CREATING!")
            object = OrderLine.objects.create(amount=validated_data['amount'], menuitem=validated_data['menuitem'], orderid=validated_data['orderid'])
            return object

class OrderLineDetailSerializer(serializers.ModelSerializer):
    #name = serializers.SerializerMethodField('get_item_name')

    # def get_item_name(self, order_line):
    #     print(order_line)
    #     object = Menu.objects.get(id=order_line.id)
    #     name = object.name
    #     return name

    class Meta:
        model = OrderLine
        fields = ('amount', 'menuitem_id')

class OrderDetailSerializer(serializers.ModelSerializer):
    lines = OrderLineDetailSerializer(source='orderlines_relation', many=True)

    class Meta:
        model = Order
        fields = ('id', 'tablenumber', 'datetime', 'lines')
