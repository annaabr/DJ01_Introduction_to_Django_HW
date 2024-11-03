from django.urls import path # data test
from . import views

urlpatterns = [
    path('', views.index),
    path('data/', views.index_data),
    path('test/', views.index_test),
]
