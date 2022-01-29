from email.policy import default
from unicodedata import category
from django.db import models
from django.utils.html import format_html

# Create your models here.
def ebook_file_format_validator(file_name) -> bool:
    """validate format file of book"""
    from django.core.exceptions import ValidationError
    formats = ('.pdf', '.epub', '.rar', '.zip', '.7z', '.tar')
    if not file_name[file_name.rfind('.'):].lower() in formats:
        raise ValidationError("Unsupported file extension.")

def audiobook_file_format_validator(file_name) -> bool:
    """validate format file of book"""
    from django.core.exceptions import ValidationError
    formats = ('.mp3', '.wav', '.wma', '.wmv', '.rar', '.zip', '.7z', '.tar')
    if not file_name[file_name.rfind('.'):].lower() in formats:
        raise ValidationError("Unsupported file extension.")


# abstract person model for inheritance author and translator model
class AbstractPerson(models.Model):
    first_name = models.CharField(max_length=75, null=False, blank=False, verbose_name="نام")
    middle_name = models.CharField(max_length=75, blank=True, default='', verbose_name="نام میانی")
    last_name = models.CharField(max_length=75, null=False, blank=False, verbose_name="نام خانوادگی")
    avatar = models.ImageField(upload_to='./images/person/', blank=True, verbose_name="عکس پروفایل")
    

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        abstract = True

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    # def show_avatar(self):
    #     full_name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name
    #     return format_html(f'<img src="{self.avatar.url}" alt="{full_name}" style="width=50px; height=50px; border-radius=50%;" />')
    # show_avatar.short_description = "پروفایل"

class Author(AbstractPerson):
    
    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"


class Translator(AbstractPerson):
    
    class Meta:
        verbose_name = "مترجم"
        verbose_name_plural = "مترجمان"


class Teller(AbstractPerson):
    
    class Meta:
        verbose_name = "گوینده"
        verbose_name_plural = "گویندگان"


class Category(models.Model):
    title = models.CharField(max_length=150, null=True, verbose_name="دسته‌بندی")
    parent = models.ForeignKey('self', default=True, null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='children', verbose_name='زیردسته')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField(max_length=256, verbose_name="نام")
    url = models.URLField(max_length=256, verbose_name="وب سایت")

    class Meta:
        verbose_name = "ناشر"
        verbose_name_plural = "ناشرین"

    def __str__(self):
        return self.title


    def show_url(self):
        return self.url[:100]
    show_url.short_description = "آدرس اینترنتی"


class Book(models.Model):
    LANGUAGE_CHOICES = (
        ('eng', 'انگلیسی'),
        ('per', 'فارسی'),
    )
    RATE_CHOICES = (
        (1, 'بد'),
        (2, 'بد نبود'),
        (3, 'معمولی'),
        (4, 'خوب'),
        (5, 'عالی'),
    )
    MONEY_UNIT = (
        ("FRE", "رایگان"),
        ("IRR", "ریال ایران"),
        ("USD", "دلار آمریکا"),
        ("GBP", "پوند انگلیس"),
        ("CAD", "دلار کانادا"),
        ("AUD", "دلار استرالیا"),
    )
    title = models.CharField(max_length=1500, verbose_name="نام کتاب")
    author = models.ManyToManyField(Author, verbose_name="نویسنده")
    translator = models.ManyToManyField(Translator, blank=True, verbose_name="مترجم")
    language_book = models.CharField(max_length=3, null=True, blank=True, choices=LANGUAGE_CHOICES, default=None, verbose_name="زبان کتاب")
    user_rate = models.SmallIntegerField(choices=RATE_CHOICES, null=True, blank=True, default=None, verbose_name="امتیاز")
    category = models.ManyToManyField(Category, blank=True, verbose_name="دسته‌بندی")
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0, verbose_name="قیمت")
    price_unit = models.CharField(max_length=3, choices=MONEY_UNIT, default="FRE", verbose_name="واحد پول")
    user_description = models.TextField(null=True, blank=True, verbose_name="توضیحات کاربر درباره کتاب")
    book_description = models.TextField(null=True, blank=True, default=None, verbose_name="توضیحات کتاب")
    book_url = models.URLField(max_length=1024, null=True, blank=True, default=None)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ناشر")

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتب"
        abstract = True

    def show_author(self):
        if self.author.all():
            return '، '.join([str(author) for author in self.author.all()])
        else:
            return '-'
    show_author.short_description = "نویسندگان"

    def show_translator(self):
        if self.translator.all():
            return '، '.join([str(translator) for translator in self.translator.all()])
        else:
            return '-'
    show_translator.short_description = "مترجمین"

    def show_category(self):
        if self.category.all():
            return '، '.join([str(category) for category in self.category.all()])
        else:
            return '-'
    show_category.short_description = "دسته‌بندی‌ها"
    

class TextBook(Book):
    READ_CHOICES = (
        ('U', "خوانده نشده"), # unread
        ('S', "در حال مطالعه"), # study
        ('R', "خوانده شده"), # read
    )
    pages_readed = models.PositiveSmallIntegerField(null= True, blank=True, verbose_name="صفحات خوانده شده")
    pages = models.PositiveSmallIntegerField(null= True, blank=True, verbose_name="تعداد صفحات کتاب")
    read_status = models.CharField(max_length=1, choices=READ_CHOICES, default='U', verbose_name='وضعیت')

    class Meta:
        verbose_name = "کتاب متنی"
        verbose_name_plural = "کتب متنی"
        abstract = True

    def __str__(self) -> str:
        return self.title


class PhysicalBook(TextBook):
    PLATFROM_LIST = (
        ("borro", "قرض گرفته شده"),
        ("prlib", "کتابخانه شخصی"),
        ("pulib", "کتابخانه عمومی"),
    )
    platform = models.CharField(max_length=5, choices=PLATFROM_LIST, null=True, blank=True, verbose_name="منبع کتاب")

    class Meta:
        verbose_name = "کتاب فیزیکی"
        verbose_name_plural = "کتب فیزیکی"

    def __str__(self) -> str:
        return self.title


class ElectronicBook(TextBook):
    PLATFROM_LIST = (
        ("taghc", "طاقچه"),
        ("ketab", "کتابراه"),
        ("fidib", "فیدیبو"),
        ("booka", "بوکاپو"),
        ("teleg", "تلگرام"),
        ("websi", "وب سایت"),
        ("prlib", "کتابخانه شخصی"),
        ("pulib", "کتابخانه عمومی"),
    )
    book_file = models.FileField(upload_to='./book_files/', null=True, blank=True, validators=[ebook_file_format_validator])
    platform = models.CharField(max_length=5, choices=PLATFROM_LIST, null=True, blank=True, verbose_name="منبع کتاب")

    class Meta:
        verbose_name = "کتاب الکترونیکی"
        verbose_name_plural = "کتب الکترونیکی"

    def __str__(self) -> str:
        return self.title


class AudioBook(Book):
    PLATFROM_LIST = (
        ("taghc", "طاقچه"),
        ("ketab", "کتابراه"),
        ("fidib", "فیدیبو"),
        ("booka", "بوکاپو"),
        ("teleg", "تلگرام"),
        ("websi", "وب سایت"),
        ("castb", "کست باکس")
    )
    LISTEN_STATUS = (
        ('U', "خوانده نشده"), # unheard
        ('L', "در حال مطالعه"), # listening
        ('H', "خوانده شده"), # heard
    )
    teller = models.ManyToManyField(Teller, blank=True, verbose_name="گوینده")
    episode = models.PositiveSmallIntegerField(null= True, blank=True, verbose_name="قسمت")
    season = models.PositiveSmallIntegerField(null= True, blank=True, verbose_name="فصل")
    listen_status = models.CharField(max_length=1, choices=LISTEN_STATUS, default='U', verbose_name="وضعیت")
    platform = models.CharField(max_length=5, choices=PLATFROM_LIST, null=True, blank=True, verbose_name="منبع کتاب")
    book_file = models.FileField(upload_to='./book_files/', null=True, blank=True, validators=[audiobook_file_format_validator])

    class Meta:
        verbose_name = "کتاب صوتی"
        verbose_name_plural = "کتب صوتی"

    def __str__(self) -> str:
        return self.title

    def show_teller(self):
        if self.teller.all():
            return '، '.join([str(teller) for teller in self.teller.all()])
        else:
            return '-'
    show_teller.short_description = "گویندگان"