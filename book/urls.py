from django.urls import path
from .views import (
    index,
    PhysicalBook,
    ElectronicBook,
    AudioBook,
    Author,
    Translator,
    Teller
)

app_name = 'book'
urlpatterns = [
    path('', index, name='index'),
    path('physicalbook/', PhysicalBook.as_view(), name='physicalbook_list'),
    path('electronicbook/', ElectronicBook.as_view(), name='electronicbook_list'),
    path('audiobook/', AudioBook.as_view(), name='audiobook_list'),
    path('author/', Author.as_view(), name='author_list'),
    path('translator/', Translator.as_view(), name='translator_list'),
    path('teller/', Teller.as_view(), name='teller_list'),
]