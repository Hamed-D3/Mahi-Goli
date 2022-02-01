from django.urls import path
from .views import index, PhysicalBook

app_name = 'book'
urlpatterns = [
    path('', index, name='index'),
    path('physicalbook/', PhysicalBook.as_view(), name='physicalbook_list'),
]