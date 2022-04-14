from multiprocessing import managers
from django.urls import path
from . import views
app_name='htmlFiles'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('filecomplaint/', views.filecomplaint, name='filecomplaint'),
    path('login/', views.login, name='login'),
    path('lookup/', views.lookup, name='lookup'),
    path('admin_lookup/', views.adminlookup, name='admin_lookup'),
    path('addoffender/',views.addoffender,name='addoffender'),
    path('view_details/',views.view_details, name='view_details'),
    path('registration/',views.registration, name='registrations'),
    path('records/',views.records, name='records'),
    path('account_manager/',views.accountmanager, name='accountmanager')
]