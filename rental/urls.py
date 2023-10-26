from django.urls import path
from . import views

urlpatterns = [
    path('rental/', views.RentList.as_view(), name='Rent List'),
    path('rental/<int:pk>/', views.RentDetail.as_view(), name='Rental Detail'),
    path('reservation/', views.ReservationList.as_view(), name='Reservation List'),
    path('reservation/<int:pk>/', views.ReservationDetail.as_view(), name='Reservation Detail'),
]
