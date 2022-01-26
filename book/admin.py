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


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_author', 'show_translator', 'show_teller', 'category', 'platform'] 
    list_filter = ['language_book', 'book_type', 'platform']
    search_fields = ['title', 'author', 'translater', 'teller', 'category', 'platform',
                        'book_file', 'user_description', 'book_description']

    


admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Teller, TellerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)