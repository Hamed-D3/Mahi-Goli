from django.shortcuts import render
from django.views.generic import ListView
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
def index(request):
    return render(request, 'book/index.html')


class PhysicalBook(ListView):
    model = PhysicalBook
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ElectronicBook(ListView):
    model = ElectronicBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AudioBook(ListView):
    model = AudioBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Author(ListView):
    model = Author
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "نویسندگان"
        return context


class Translator(ListView):
    model = Translator
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "مترجمین"
        return context


class Teller(ListView):
    model = Teller
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "گویندگان"
        return context


class Publisher(ListView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Category(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context