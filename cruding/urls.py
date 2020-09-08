from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.crudingUpdate, name="update_task"),
    path('delete_task/<str:pk>/', views.crudingDelete, name="delete_task"),
]