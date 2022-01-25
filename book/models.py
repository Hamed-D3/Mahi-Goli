from django.db import models
from django.utils.html import format_html

# Create your models here.
def file_format_validator(file_name) -> bool:
    """validate format file of book"""
    from django.core.exceptions import ValidationError
    formats = ('.pdf', '.epub', '.rar', '.zip')
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


class Publisher(models.Model):
    title = models.CharField(max_length=256, verbose_name="نام")
    url = models.URLField(max_length=256, verbose_name="وب سایت")

    class Meta:
        verbose_name = "ناشر"
        verbose_name_plural = "ناشرین"


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
    BOOK_TYPES = (
        ('a', 'صوتی'),
        ('p', 'فیزیکی'),
        ('e', 'الکترونیکی'),
    )
    MONEY_UNIT = (
        ("IRR", "ریال ایران"),
        ("USD", "دلار آمریکا"),
        ("GBP", "پوند انگلیس"),
        ("CAD", "دلار کانادا"),
        ("AUD", "دلار استرالیا"),
    )
    PLATFROM_LIST = (
        ("taghc", "طاقچه"),
        ("ketab", "کتابراه"),
        ("teleg", "تلگرام"),
        ("websi", "وب سایت"),
        ("prlib", "کتابخانه شخصی"),
        ("pulib", "کتابخانه عمومی"),
    )
    title = models.CharField(max_length=1500, verbose_name="نام کتاب")
    author = models.ManyToManyField(Author, verbose_name="نویسنده")
    translator = models.ManyToManyField(Translator, blank=True, verbose_name="مترجم")
    teller = models.ManyToManyField(Teller, blank=True, verbose_name="گوینده")
    language_book = models.CharField(max_length=3, choices=LANGUAGE_CHOICES, default="per")
    book_url = models.URLField(max_length=1024, null=True, blank=True, default=None)
    book_file = models.FileField(upload_to='./book_files/', blank=True, validators=[file_format_validator])
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="دسته‌بندی")
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="قیمت")
    price_unit = models.CharField(max_length=3, choices=MONEY_UNIT, default="IRR", verbose_name="واحد پول")
    user_description = models.TextField(null=True, blank=True, verbose_name="توضیحات کاربر درباره کتاب")
    rate = models.SmallIntegerField(choices=RATE_CHOICES, null=True, blank=True, verbose_name="امتیاز")
    book_type = models.CharField(max_length=1, choices=BOOK_TYPES, default="e", verbose_name="نوع کتاب")
    pages_readed = models.PositiveSmallIntegerField(null= True, blank=True, verbose_name="صفحات خوانده شده")
    pages = models.PositiveSmallIntegerField(null= True, blank=True, verbose_name="تعداد صفحات کتاب")
    book_description = models.TextField(null=True, blank=True, default=None, verbose_name="توضیحات کتاب")
    platform = models.CharField(max_length=5, null=True, blank=True, verbose_name="منبع کتاب")


    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتب"

    def __str__(self) -> str:
        return self.title