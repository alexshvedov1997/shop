from django.urls import path
from .views import  ProductList, product_detail

urlpatterns = [
    path('', ProductList.as_view(), name = 'product_list'),
    path('product_detail/<int:id>/<slug:slug>/', product_detail, name = "detail")
]