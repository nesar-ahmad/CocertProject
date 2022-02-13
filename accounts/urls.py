from unicodedata import name
from django.urls import path
from .import views


app_name='accounts'

urlpatterns = [
    path('login/', views.loginView, name='log_in'),
    path('logout/', views.logoutView, name='log_out'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
]