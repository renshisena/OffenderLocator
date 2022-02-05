from django.urls import path
from . import views
app_name='htmlFiles'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('filecomplaint/', views.filecomplaint, name='filecomplaint'),
    path('login/', views.login, name='login'),
    path('reset/', views.reset, name='reset'),
    path('lookup/', views.lookup, name='lookup'),
    path('admin_lookup/', views.adminlookup, name='admin_lookup'),
    path('results/', views.results, name='results'),
    path('addoffender/',views.addoffender,name='addoffender'),
    path('showoffenders/',views.showoffenders, name='showoffenders'),
]