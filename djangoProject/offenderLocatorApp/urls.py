from multiprocessing import managers
from re import template
from django.conf import settings
from django.urls import path
# from mysqlx import Auth
from . import views
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
app_name='htmlFiles'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('filecomplaint/', views.filecomplaint, name='filecomplaint'),
    path('login/', views.loginpage, name ='login'),
    path('lookup/', views.lookup, name='lookup'),
    path('admin_lookup/', views.adminlookup, name='admin_lookup'),
    path('addoffender/',views.addoffender,name='addoffender'),
    path('view_details/',views.view_details, name='view_details'),
    path('registration/',views.user_registration, name='registration'),
    path('records/',views.records, name='records'),
    path('account_manager/',views.accountmanager, name='accountmanager'),
    path('about/',views.about, name='about'),
    path('logout/',views.logoutUser, name='logout'),
    path('schedule/',views.schedule, name='schedule'),
    # path('opensched/',views.opensched, name='opensched'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)