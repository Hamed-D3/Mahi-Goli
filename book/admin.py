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


admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Teller, TellerAdmin)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book)