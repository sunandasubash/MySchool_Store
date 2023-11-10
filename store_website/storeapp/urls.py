from django.urls import path

from storeapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('studentform/',views.studentform,name='studentform'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('success/', views.success, name='success'),
]