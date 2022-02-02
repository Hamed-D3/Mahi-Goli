from django.shortcuts import render
from django.views.generic import ListView
from .models import PhysicalBook, ElectronicBook

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