from django.urls import path
from car_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car_detail/<str:manufacturer>/<str:model_name>/', views.car_detail, name='car_detail'),
]
