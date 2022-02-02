from django.urls import path
from .views import index, PhysicalBook, ElectronicBook, AudioBook

app_name = 'book'
urlpatterns = [
    path('', index, name='index'),
    path('physicalbook/', PhysicalBook.as_view(), name='physicalbook_list'),
    path('electronicbook/', ElectronicBook.as_view(), name='electronicbook_list'),
    path('audiobook/', AudioBook.as_view(), name='audiobook_list'),
]