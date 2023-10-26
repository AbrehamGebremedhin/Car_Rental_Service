from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.ReviewList.as_view(), name='Review List'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='Review Detail'),
]
