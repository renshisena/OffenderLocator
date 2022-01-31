from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('filecomplaint/', views.filecomplaint, name='filecomplaint'),
    path('login/', views.login, name='login'),
    path('reset/', views.reset, name='reset'),
    path('lookup/', views.lookup, name='lookup'),
]