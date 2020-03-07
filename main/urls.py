from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('<str:page>', views.other_page, name='other'),
    path('accounts/login', views.BBLoginView.as_view(), name='login'),
    path('accounts/logout', views.BBLogoutView.as_view(), name='logout'),
    path('accounts/profile', views.profile, name='profile'),
    path('', views.index, name='index'),


    ]