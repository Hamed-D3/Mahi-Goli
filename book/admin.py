from django.contrib import admin
from book.models import *

# Register your models here.
@admin.action(description="خوانده نشدن کتاب‌های انتخاب شده")
def make_unread(modeladmin, request, queryset):
    rows_updated = queryset.update(read_status='U')
    if rows_updated == 1:
        message_bit = "به وضعیت خوانده نشده رفت."
    else:
        message_bit = "به وضعیت خوانده نشده رفتند."
    modeladmin.message_user(request, f"{rows_updated} کتاب {message_bit}")


@admin.action(description="در حال مطالعه شدن کتاب‌های انتخاب شده")
def make_study(modeladmin, request, queryset):
    rows_updated = queryset.update(read_status='S')
    if rows_updated == 1:
        message_bit = "به وضعیت در حال مطالعه رفت."
    else:
        message_bit = "به وضعیت در حال مطالعه رفتند."
    modeladmin.message_user(request, f"{rows_updated} کتاب {message_bit}")


@admin.action(description="خوانده شدن کتاب‌های انتخاب شده")
def make_read(modeladmin, request, queryset):
    rows_updated = queryset.update(read_status='R')
    if rows_updated == 1:
        message_bit = "به وضعیت خوانده شده رفت."
    else:
        message_bit = "به وضعیت خوانده شده رفتند."
    modeladmin.message_user(request, f"{rows_updated} کتاب {message_bit}")


@admin.action(description="شنیده نشدن کتاب‌های انتخاب شده")
def make_unheard(modeladmin, request, queryset):
    rows_updated = queryset.update(listen_status='U')
    if rows_updated == 1:
        message_bit = "به وضعیت شنیده نشده رفت."
    else:
        message_bit = "به وضعیت شنیده نشده رفتند."
    modeladmin.message_user(request, f"{rows_updated} کتاب صوتی {message_bit}")


@admin.action(description="در حال شنیدن کتاب‌های صوتی انتخاب شده")
def make_listening(modeladmin, request, queryset):
    rows_updated = queryset.update(listen_status='L')
    if rows_updated == 1:
        message_bit = "به وضعیت در حال شنیدن رفت."
    else:
        message_bit = "به وضعیت در حال شنیدن رفتند."
    modeladmin.message_user(request, f"{rows_updated} کتاب صوتی {message_bit}")


@admin.action(description="شنیده شدن کتاب‌های صوتی انتخاب شده")
def make_heard(modeladmin, request, queryset):
    rows_updated = queryset.update(listen_status='H')
    if rows_updated == 1:
        message_bit = "به وضعیت شنیده شده رفت."
    else:
        message_bit = "به وضعیت شنیده شده رفتند."
    modeladmin.message_user(request, f"{rows_updated} کتاب صوتی {message_bit}")


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
    list_display = ['title', 'show_author', 'show_translator', 'show_category', 'publisher', 'platform', 'user_rate', 'read_status'] 
    list_filter = ['language_book', 'platform', 'read_status', 'category', 'user_rate']
    search_fields = ['title', 'author', 'translater', 'category', 'user_description', 'book_description']
    actions = [make_unread, make_study, make_read]


class ElectronicBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_author', 'show_translator', 'show_category', 'publisher', 'platform', 'user_rate', 'read_status'] 
    list_filter = ['language_book', 'platform', 'read_status', 'category', 'user_rate']
    search_fields = ['title', 'author', 'translater', 'category', 'user_description', 'book_description']
    actions = [make_unread, make_study, make_read]


class AudioBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_author', 'show_translator', 'show_teller', 'show_category', 'publisher', 'platform', 'user_rate', 'listen_status'] 
    list_filter = ['language_book', 'platform', 'listen_status', 'category', 'user_rate']
    search_fields = ['title', 'author', 'translater', 'category', 'user_description', 'book_description']
    actions = [make_unheard, make_listening, make_heard]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(Teller, TellerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(PhysicalBook, PhysicalBookAdmin)
admin.site.register(ElectronicBook, ElectronicBookAdmin)
admin.site.register(AudioBook, AudioBookAdmin)