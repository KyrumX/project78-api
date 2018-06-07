from django.urls import path

from API.views import MenuList, MenuDetail, OrderList, OrderDetailLine, OrderLineDetail, OrderSum

urlpatterns = [
    path('menu/', MenuList.as_view()),
    path('menu/<int:pk>', MenuDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>', OrderDetailLine.as_view()),
    path('orders/sum/<int:pk>', OrderSum.as_view()),
    path('orderlines/', OrderLineDetail.as_view()),
]