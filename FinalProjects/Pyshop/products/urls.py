from django.urls import path
from . import views

# /products --> root
# / product/details

urlpatterns = [
    path('',views.index),
    path('newproduct',views.newproduct)
]