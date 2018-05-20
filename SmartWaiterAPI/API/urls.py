from django.urls import path

from API.views import MenuList, MenuDetail, OrderList, OrderDetail

urlpatterns = [
    path('menu/', MenuList.as_view()),
    path('menu/<int:pk>', MenuDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>', OrderDetail.as_view()),
]