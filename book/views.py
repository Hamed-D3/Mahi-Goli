import random
from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from book.forms import (
    AudioBookCreateUpdateForm,
    PhysicalBookCreateUpdateForm,
    ElectronicBookCreateUpdateForm,
)
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
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
class HomeView(TemplateView):
    template_name = 'book/index.html'


class AllBookView(TemplateView):

    def get(self, request, **kwargs):
        all_book = []

        physicalbook = PhysicalBook.objects.filter(user=self.request.user).all()
        electronicbook = ElectronicBook.objects.filter(user=self.request.user).all()
        audiobook = AudioBook.objects.filter(user=self.request.user).all()

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
                'type': 'فیزیکی',
                'update_url': reverse('book:physicalbook_update', kwargs={'pk':book.pk}),
                'delete_url': reverse('book:physicalbook_delete', kwargs={'pk':book.pk}),
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
                'type': 'الکترونیکی',
                'update_url': reverse('book:electronicbook_update', kwargs={'pk':book.pk}),
                'delete_url': reverse('book:electronicbook_delete', kwargs={'pk':book.pk}),
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
                'type': 'صوتی',
                'update_url': reverse('book:audiobook_update', kwargs={'pk':book.pk}),
                'delete_url': reverse('book:audiobook_delete', kwargs={'pk':book.pk}),
            })

        random.shuffle(all_book)
        context = {
            'all_book': all_book
        }

        return render(request, 'book/books.html', context)


class PhysicalBookListView(ListView):
    model = PhysicalBook
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ElectronicBookListView(ListView):
    model = ElectronicBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AudioBookListView(ListView):
    model = AudioBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AuthorListView(ListView):
    model = Author
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "نویسندگان"
        context['update_url'] = 'book:author_update'
        context['delete_url'] = 'book:author_delete'
        return context


class TranslatorListView(ListView):
    model = Translator
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "مترجمین"
        context['update_url'] = 'book:translator_update'
        context['delete_url'] = 'book:translator_delete'
        return context


class TellerListView(ListView):
    model = Teller
    template_name = 'book/person_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_title'] = "گویندگان"
        context['update_url'] = 'book:teller_update'
        context['delete_url'] = 'book:teller_delete'
        return context


class PublisherListView(ListView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PhysicalBookCreateView(SuccessMessageMixin, CreateView):
    model = PhysicalBook
    form_class = PhysicalBookCreateUpdateForm
    template_name = 'book/physicalbook_create_update.html'
    success_message = "کتاب فیزیکی با موفقیت افزوده شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PhysicalBookUpdateView(SuccessMessageMixin, UpdateView):
    model = PhysicalBook
    form_class = PhysicalBookCreateUpdateForm
    template_name = 'book/physicalbook_create_update.html'
    success_message = "کتاب فیزیکی با موفقیت ویرایش شد"


class PhysicalBookDeleteView(SuccessMessageMixin, DeleteView):
    model = PhysicalBook
    success_url = reverse_lazy('book:physicalbook')
    template_name = 'book/book_confirm_delete.html'
    success_message = "کتاب فیزیکی با موفقیت حذف شد"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PhysicalBookDeleteView, self).delete(request, *args, **kwargs)


class ElectronicBookCreateView(SuccessMessageMixin, CreateView):
    model = ElectronicBook
    form_class = ElectronicBookCreateUpdateForm
    template_name = 'book/electronicbook_create_update.html'
    success_message = "کتاب الکترونیکی با موفقیت افزوده شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ElectronicBookUpdateView(SuccessMessageMixin, UpdateView):
    model = ElectronicBook
    form_class = ElectronicBookCreateUpdateForm
    template_name = 'book/electronicbook_create_update.html'
    success_message = "کتاب الکترونیکی با موفقیت ویرایش شد"


class ElectronicBookDeleteView(DeleteView):
    model = ElectronicBook
    success_url = reverse_lazy('book:electronicbook')
    template_name = 'book/book_confirm_delete.html'
    success_message = "کتاب الکترونیکی با موفقیت حذف شد"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ElectronicBookDeleteView, self).delete(request, *args, **kwargs)


class AudioBookCreateView(SuccessMessageMixin, CreateView):
    model = AudioBook
    form_class = AudioBookCreateUpdateForm
    template_name = 'book/audiobook_create_update.html'
    success_message = "کتاب صوتی با موفقیت افزوده شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AudioBookUpdateView(SuccessMessageMixin, UpdateView):
    model = AudioBook
    form_class = AudioBookCreateUpdateForm
    template_name = 'book/audiobook_create_update.html'
    success_message = "کتاب صوتی با موفقیت ویرایش شد"


class AudioBookDeleteView(DeleteView):
    model = AudioBook
    success_url = reverse_lazy('book:audiobook')
    template_name = 'book/book_confirm_delete.html'
    success_message = "کتاب صوتی با موفقیت حذف شد"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AudioBookDeleteView, self).delete(request, *args, **kwargs)


class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Author
    fields = ['avatar', 'first_name', 'last_name']
    template_name = 'book/person_create_update.html'
    success_message = "نویسنده با موفقیت افزوده شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Author._meta.verbose_name
        return context


class AuthorUpdateView(SuccessMessageMixin, UpdateView):
    model = Author
    fields = ['avatar', 'first_name', 'last_name']
    template_name = 'book/person_create_update.html'
    success_message = "نویسنده با موفقیت ویرایش شد"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Author._meta.verbose_name
        return context


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('book:author')
    template_name = 'book/person_confirm_delete.html'
    success_message = "نویسنده با موفقیت حذف شد"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Author._meta.verbose_name
        context['model_name_plural'] = Author._meta.verbose_name_plural
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AuthorDeleteView, self).delete(request, *args, **kwargs)


class TranslatorCreateView(SuccessMessageMixin, CreateView):
    model = Translator
    fields = ['avatar', 'first_name', 'last_name']
    template_name = 'book/person_create_update.html'
    success_message = "مترجم با موفقیت افزوده شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Translator._meta.verbose_name
        return context


class TranslatorUpdateView(SuccessMessageMixin, UpdateView):
    model = Translator
    fields = ['avatar', 'first_name', 'last_name']
    template_name = 'book/person_create_update.html'
    success_message = "مترجم با موفقیت ویرایش شد"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Translator._meta.verbose_name
        return context


class TranslatorDeleteView(DeleteView):
    model = Translator
    success_url = reverse_lazy('book:translator')
    template_name = 'book/person_confirm_delete.html'
    success_message = "مترجم با موفقیت حذف شد"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Translator._meta.verbose_name
        context['model_name_plural'] = Translator._meta.verbose_name_plural
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TranslatorDeleteView, self).delete(request, *args, **kwargs)


class TellerCreateView(SuccessMessageMixin, CreateView):
    model = Translator
    fields = ['avatar', 'first_name', 'last_name']
    template_name = 'book/person_create_update.html'
    success_message = "گوینده با موفقیت افزوده شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Teller._meta.verbose_name
        return context


class TellerUpdateView(SuccessMessageMixin, UpdateView):
    model = Translator
    fields = ['avatar', 'first_name', 'last_name']
    template_name = 'book/person_create_update.html'
    success_message = "گوینده با موفقیت ویرایش شد"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Teller._meta.verbose_name
        return context


class TellerDeleteView(DeleteView):
    model = Teller
    success_url = reverse_lazy('book:teller')
    template_name = 'book/person_confirm_delete.html'
    success_message = "گوینده با موفقیت حذف شد"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = Teller._meta.verbose_name
        context['model_name_plural'] = Teller._meta.verbose_name_plural
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TranslatorDeleteView, self).delete(request, *args, **kwargs)


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    fields = ['title', 'parent']
    template_name = 'book/category_create_update.html'
    success_message = "دسته‌بندی با موفقیت افزوده شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    fields = ['title', 'parent']
    template_name = 'book/category_create_update.html'
    success_message = "دسته‌بندی با موفقیت ویرایش شد"


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('book:category')
    template_name = 'book/category_confirm_delete.html'
    success_message = "دسته‌بندی با موفقیت حذف شد"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CategoryDeleteView, self).delete(request, *args, **kwargs)


class PublisherCreateView(SuccessMessageMixin, CreateView):
    model = Publisher
    fields = ['title', 'url']
    template_name = 'book/publisher_create_update.html'
    success_message = "ناشر با موفقیت افزوده شد"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PublisherUpdateView(SuccessMessageMixin, UpdateView):
    model = Publisher
    fields = ['title', 'url']
    template_name = 'book/publisher_create_update.html'
    success_message = "ناشر با موفقیت ویرایش شد"


class PublisherDeleteView(DeleteView):
    model = Publisher
    success_url = reverse_lazy('book:publisher')
    template_name = 'book/publisher_confirm_delete.html'
    success_message = "ناشر با موفقیت حذف شد"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PublisherDeleteView, self).delete(request, *args, **kwargs)