from django.urls import path
from .views import (
    index,
    PhysicalBookList,
    ElectronicBookList,
    AudioBookList,
    AuthorList,
    TranslatorList,
    TellerList,
    PublisherList,
    CategoryList,
)

app_name = 'book'
urlpatterns = [
    path('', index, name='index'),
    path('physicalbook/', PhysicalBookList.as_view(), name='physicalbook'),
    path('electronicbook/', ElectronicBookList.as_view(), name='electronicbook'),
    path('audiobook/', AudioBookList.as_view(), name='audiobook'),
    path('author/', AuthorList.as_view(), name='author'),
    path('translator/', TranslatorList.as_view(), name='translator'),
    path('teller/', TellerList.as_view(), name='teller'),
    path('publisher/', PublisherList.as_view(), name='publisher'),
    path('category/', CategoryList.as_view(), name='category'),
]