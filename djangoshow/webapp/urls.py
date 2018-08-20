from django.urls import path, include
from webapp import views

urlpatterns = [
    path(r'shijing/', views.shijingtest)
]