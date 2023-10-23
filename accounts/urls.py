from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.CreateUser.as_view(), name="Create User"),
    path('customers/', views.CreateCustomer.as_view(), name='Create Customer'),
    path('customer/<int:pk>/', views.CustomerDetail.as_view(), name='Customer Detail'),
]
