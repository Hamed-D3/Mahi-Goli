from django.contrib import admin
from book.models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Translator)
admin.site.register(Teller)
admin.site.register(Category)
admin.site.register(Book)