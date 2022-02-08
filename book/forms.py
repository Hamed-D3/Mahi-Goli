from django.forms import ModelForm
from book.widgets import CustomeClearableFileInput
from book.models import AudioBook, PhysicalBook, ElectronicBook

class PhysicalBookCreateUpdateForm(ModelForm):

    class Meta:
        model = PhysicalBook
        fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher', 'pages_readed', 'pages', 'read_status', 'platform']
        widgets = {
            'picture': CustomeClearableFileInput(),
        }


class ElectronicBookCreateUpdateForm(ModelForm):

    class Meta:
        model = ElectronicBook
        fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher', 'pages_readed', 'pages', 'read_status', 'platform', 'book_file']
        widgets = {
            'picture': CustomeClearableFileInput(),
        }


class AudioBookCreateUpdateForm(ModelForm):

    class Meta:
        model = AudioBook
        fields = ['picture', 'title', 'author', 'translator', 'language_book', 'user_rate', 'category', 'price', 'price_unit', 'user_description', 'book_url', 'publisher',  'teller', 'episode', 'season', 'listen_status', 'platform', 'book_file']
        widgets = {
            'picture': CustomeClearableFileInput(),
        }