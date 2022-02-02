from django.urls import path
from .views import (
    index,
    PhysicalBook,
    ElectronicBook,
    AudioBook,
    Author,
    Translator,
    Teller,
    Publisher,
    Category,
)

app_name = 'book'
urlpatterns = [
    path('', index, name='index'),
    path('physicalbook/', PhysicalBook.as_view(), name='physicalbook'),
    path('electronicbook/', ElectronicBook.as_view(), name='electronicbook'),
    path('audiobook/', AudioBook.as_view(), name='audiobook'),
    path('author/', Author.as_view(), name='author'),
    path('translator/', Translator.as_view(), name='translator'),
    path('teller/', Teller.as_view(), name='teller'),
    path('publisher/', Publisher.as_view(), name='publisher'),
    path('category/', Category.as_view(), name='category'),
]