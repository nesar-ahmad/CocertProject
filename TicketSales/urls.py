from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from . import views


app_name = 'TicketSales'

urlpatterns = [
    path('', views.concert_list, name='concert_list'),
    path('concert/<int:concert_id>', views.concert_detail, name='concert_detail'),
    path('location/list', views.concert_location, name='concert_location'),
    path('time/list', views.time_list, name='time_list'),
    path('concert/<int:concert_id>/eidt',
        views.concert_edit, name='concert_edit'),
]