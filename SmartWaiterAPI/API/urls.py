from django.urls import path

from API.views import MenuList, MenuDetail, OrderList, OrderDetailLine, OrderLineDetail

urlpatterns = [
    path('menu/', MenuList.as_view()),
    path('menu/<int:pk>', MenuDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>', OrderDetailLine.as_view()),
    path('orderlines/', OrderLineDetail.as_view()),
]