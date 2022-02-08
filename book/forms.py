from django.forms import ModelForm
from book.widgets import CustomeClearableFileInput
from book.models import PhysicalBook

class PhysicalBookCreateUpdateForm(ModelForm):

    class Meta:
        model = PhysicalBook
        fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher', 'pages_readed', 'pages', 'read_status', 'platform']
        widgets = {
            'picture': CustomeClearableFileInput(),
        }