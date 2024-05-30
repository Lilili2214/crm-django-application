from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name= ""),
    path("register", views.register, name="register"),
    path("my-login", views.my_login, name='login'),
    path("logout", views.user_logout, name='logout'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("create_record", views.create_record, name='create_record'),
    path('update-record/<int:pk>', views.udpate_record, name='update-record'),
    path('record/<int:pk>', views.view_singular, name='view-record'),

] 