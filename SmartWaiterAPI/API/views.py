from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from API import serializers
from API.collections.goeswellwith_operations import get_goeswellwith_items
from API.collections.order_operations import get_order_sum
from API.models import Menu, Order, OrderLine, GoesWellWith

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
class OrderDetailLine(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer


"""
    This is the order list API View
    it displays all the placed orderlines
    in a list format including all
    the details.
    This endpoint allows: CREATING, GET

    URL: api/orderlines/
"""
class OrderLineDetail(generics.ListCreateAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = serializers.OrderLineDetailCreatorSerializer

"""
    This view will return the total amount of
    money to be paid by the customer.

    URL: api/orders/sum/<int:id>
"""

class OrderSum(APIView):
    def get(self, request, pk):
        sum = get_order_sum(pk)

        return Response({'sum': sum})


"""
    This returns all the names of the items
    that go well with a requested item.

    URL: api/goeswellwith/<int:menuitem1>
"""

class GoesWellWithView(APIView):
    def get(self, request, menuitem1):
        items = get_goeswellwith_items(menuitem1)

        return Response(items)
