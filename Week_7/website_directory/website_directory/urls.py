from django.urls import path
from directory_app import views

urlpatterns = [
    path('add_category/', views.add_category, name='add_category'),
    path('add_page/', views.add_page, name='add_page'),
    path('', views.index, name='index'),
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
]