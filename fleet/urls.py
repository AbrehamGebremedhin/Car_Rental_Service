from django.urls import path
from . import views

urlpatterns = [
    path('fleet/', views.VehicleList.as_view(), name='Vehicle List'),
    path('fleet/<int:pk>/', views.VehicleDetail.as_view(), name='Vehicle Detail'),
    path('maintenance/all/<int:pk>/', views.MaintenanceList.as_view(), name='Maintenance List'),
    path('maintenance/<int:pk>/', views.MaintenanceDetail.as_view(), name='Maintenance Detail'),
]
