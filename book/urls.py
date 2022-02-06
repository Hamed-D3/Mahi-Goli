from django.urls import path
from .views import (
    AllBook,
    PhysicalBookList,
    ElectronicBookList,
    AudioBookList,
    AuthorList,
    TranslatorList,
    TellerList,
    PublisherList,
    CategoryList,
    PhysicalBookCreate,
    ElectronicBookCreate,
    AudioBookCreate,
    PhysicalBookUpdate,
)

app_name = 'book'
urlpatterns = [
    path('', AllBook.as_view(), name='allbook'),
    path('physicalbook/', PhysicalBookList.as_view(), name='physicalbook'),
    path('electronicbook/', ElectronicBookList.as_view(), name='electronicbook'),
    path('audiobook/', AudioBookList.as_view(), name='audiobook'),
    path('author/', AuthorList.as_view(), name='author'),
    path('translator/', TranslatorList.as_view(), name='translator'),
    path('teller/', TellerList.as_view(), name='teller'),
    path('publisher/', PublisherList.as_view(), name='publisher'),
    path('category/', CategoryList.as_view(), name='category'),
    path('physicalbook/create/', PhysicalBookCreate.as_view(), name='physicalbook_create'),
    path('physicalbook/update/<int:pk>', PhysicalBookUpdate.as_view(), name='physicalbook_update'),
    path('electronicbook/create/', ElectronicBookCreate.as_view(), name='electronicbook_create'),
    path('audiobook/create/', AudioBookCreate.as_view(), name='audiobook_create'),
]