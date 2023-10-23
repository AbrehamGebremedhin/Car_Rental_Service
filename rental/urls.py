from django.urls import path
from . import views

urlpatterns = [
    path('rental/', views.RentList.as_view(), name='Rent List'),
    path('rental/<int:pk>/', views.RentDetail.as_view(), name='Rental Detail'),
]
