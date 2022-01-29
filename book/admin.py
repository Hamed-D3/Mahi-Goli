from django.contrib import admin
from book.models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name']
    search_fields = ['first_name', 'middle_name', 'last_name']
    

class TranslatorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name']
    search_fields = ['first_name', 'middle_name', 'last_name']


class TellerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name']
    search_fields = ['first_name', 'middle_name', 'last_name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']
    search_fields = ['title', 'parent']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_url']
    search_fields = ['title']


class PhysicalBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_author', 'show_translator', 'show_category', 'platform', 'user_rate', 'read_flag'] 
    list_filter = ['language_book', 'platform', 'read_flag', 'category', 'user_rate']
    search_fields = ['title', 'author', 'translater', 'category', 'user_description', 'book_description']


class ElectronicBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_author', 'show_translator', 'show_category', 'platform', 'user_rate', 'read_flag'] 
    list_filter = ['language_book', 'platform', 'read_flag', 'category', 'user_rate']
    search_fields = ['title', 'author', 'translater', 'category', 'user_description', 'book_description']


class AudioBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_author', 'show_translator', 'show_teller', 'show_category', 'platform', 'user_rate', 'listen_flag'] 
    list_filter = ['language_book', 'platform', 'listen_flag', 'category', 'user_rate']
    search_fields = ['title', 'author', 'translater', 'category', 'user_description', 'book_description']
    


admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Teller, TellerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(PhysicalBook, PhysicalBookAdmin)
admin.site.register(ElectronicBook, ElectronicBookAdmin)
admin.site.register(AudioBook, AudioBookAdmin)