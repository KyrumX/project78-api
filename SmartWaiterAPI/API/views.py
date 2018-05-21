from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from API import serializers
from API.models import Menu, Order, OrderLine

"""
    This is the menu list API View
    it displays all menu items
    in a list format with all
    details.

    URL: api/menu/
"""
class MenuList(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer


"""
    This is the menu detail API View
    it displays all the details of
    a single menu item.

    URL: api/menu/<int:id>
"""
class MenuDetail(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuDetailSerializer


"""
    This is the order list API View
    it displays all the placed orders
    in a list format including all
    the details.

    URL: api/orders/
"""
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


"""
    This is the order detail API View
    it displays all the details of
    a single order.

    URL: api/orders/<int:id>
"""
class OrderDetail(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer


