import random
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from .models import (
    PhysicalBook,
    ElectronicBook,
    AudioBook,
    Author,
    Translator,
    Teller,
    Publisher,
    Category,
)

# Create your views here.
class AllBook(TemplateView):

    def get(self, request, **kwargs):
        all_book = []

        physicalbook = PhysicalBook.objects.all()
        electronicbook = ElectronicBook.objects.all()
        audiobook = AudioBook.objects.all()

        for book in physicalbook:
            all_book.append({
                'picture': book.picture,
                'title': book.title,
                'show_author': book.show_author,
                'show_translator': book.show_translator,
                'show_category': book.show_category,
                'show_publisher': book.show_publisher,
                'show_user_rate': book.show_user_rate,
                'status': book.get_read_status_display(),
                'platform': book.get_platform_display(),
                'type': 'فیزیکی'
            })
        
        for book in electronicbook:
            all_book.append({
                'picture': book.picture,
                'title': book.title,
                'show_author': book.show_author,
                'show_translator': book.show_translator,
                'show_category': book.show_category,
                'show_publisher': book.show_publisher,
                'show_user_rate': book.show_user_rate,
                'status': book.get_read_status_display(),
                'platform': book.get_platform_display(),
                'type': 'الکترونیکی'
            })

        for book in audiobook:
            all_book.append({
                'picture': book.picture,
                'title': book.title,
                'show_author': book.show_author,
                'show_translator': book.show_translator,
                'show_category': book.show_category,
                'show_publisher': book.show_publisher,
                'show_user_rate': book.show_user_rate,
                'status': book.get_listen_status_display(),
                'platform': book.get_platform_display(),
                'type': 'صوتی'
            })

        random.shuffle(all_book)
        context = {
            'all_book': all_book
        }

        return render(request, 'book/index.html', context)


class PhysicalBookList(ListView):
    model = PhysicalBook
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ElectronicBookList(ListView):
    model = ElectronicBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AudioBookList(ListView):
    model = AudioBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AuthorList(ListView):
    model = Author
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "نویسندگان"
        return context


class TranslatorList(ListView):
    model = Translator
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "مترجمین"
        return context


class TellerList(ListView):
    model = Teller
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "گویندگان"
        return context


class PublisherList(ListView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryList(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhysicalBookCreate(CreateView):
    model = PhysicalBook
    fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher', 'pages_readed', 'pages', 'read_status', 'platform']
    template_name = 'book/physicalbook_create_update.html'