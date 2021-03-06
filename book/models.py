from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

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
    last_name = models.CharField(max_length=75, null=False, blank=False, verbose_name="نام خانوادگی")
    avatar = models.ImageField(upload_to='images/person/', blank=True, verbose_name="عکس پروفایل")
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        abstract = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Author(AbstractPerson):
    
    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"

    def get_absolute_url(self):
        return reverse('book:author')


class Translator(AbstractPerson):
    
    class Meta:
        verbose_name = "مترجم"
        verbose_name_plural = "مترجمان"

    def get_absolute_url(self):
        return reverse('book:translator')


class Teller(AbstractPerson):
    
    class Meta:
        verbose_name = "گوینده"
        verbose_name_plural = "گویندگان"

    def get_absolute_url(self):
        return reverse('book:teller')


class Category(models.Model):
    title = models.CharField(max_length=150, null=True, verbose_name="دسته‌بندی")
    parent = models.ForeignKey('self', default=True, null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='children', verbose_name='زیردسته')
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title

    def show_parent(self):
        if self.parent:
            return self.parent
        else:
            return '-'
    show_parent.short_description = 'زیر دسته'

    def get_absolute_url(self):
        return reverse('book:category')


class Publisher(models.Model):
    title = models.CharField(max_length=256, verbose_name="نام")
    url = models.URLField(max_length=256, verbose_name="وب سایت")
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "ناشر"
        verbose_name_plural = "ناشرین"

    def __str__(self):
        return self.title


    def show_url(self):
        return self.url[:100]
    show_url.short_description = "آدرس اینترنتی"

    def get_absolute_url(self):
        return reverse('book:publisher')


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
        ("FRE", "---"),
        ("IRR", "تومان ایران"),
        ("USD", "دلار آمریکا"),
        ("GBP", "پوند انگلیس"),
        ("CAD", "دلار کانادا"),
        ("AUD", "دلار استرالیا"),
    )
    picture = models.ImageField(upload_to='images/books/', blank=True, verbose_name='تصویر جلد')
    title = models.CharField(max_length=1500, verbose_name="نام کتاب")
    author = models.ManyToManyField(Author, verbose_name="نویسنده")
    translator = models.ManyToManyField(Translator, blank=True, verbose_name="مترجم")
    language_book = models.CharField(max_length=3, null=True, blank=True, choices=LANGUAGE_CHOICES, default=None, verbose_name="زبان کتاب")
    user_rate = models.SmallIntegerField(choices=RATE_CHOICES, null=True, blank=True, default=None, verbose_name="امتیاز")
    category = models.ManyToManyField(Category, blank=True, verbose_name="دسته‌بندی")
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, default=0, verbose_name="قیمت")
    price_unit = models.CharField(max_length=3, choices=MONEY_UNIT, null=True, blank=True, default="FRE", verbose_name="واحد پول")
    user_description = models.TextField(null=True, blank=True, verbose_name="توضیحات کاربر درباره کتاب")
    book_description = models.TextField(null=True, blank=True, default=None, verbose_name="توضیحات کتاب")
    book_url = models.URLField(max_length=1024, null=True, blank=True, default=None, verbose_name="آدرس اینترنتی")
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="ناشر")
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)

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

    def show_user_rate(self):
        if self.user_rate == None:
            return '-'
        else:
            return self.user_rate
    show_user_rate.short_description = "تصویر جلد"

    def show_publisher(self):
        if self.publisher:
            return self.publisher
        else:
            return '-'
    

class TextBook(Book):
    READ_CHOICES = (
        ('U', "خوانده نشده"), # unread
        ('S', "در حال مطالعه"), # study
        ('R', "خوانده شده"), # read
        ('M', "نشان شده"), # mark
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

    def show_platform(self):
        if self.platform:
            return self.get_platform_display()
        else:
            return '-'

    def get_absolute_url(self):
        return reverse('book:physicalbook')


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
    book_file = models.FileField(upload_to='electronicbook_files/', null=True, blank=True, validators=[ebook_file_format_validator])
    platform = models.CharField(max_length=5, choices=PLATFROM_LIST, null=True, blank=True, verbose_name="منبع کتاب")

    class Meta:
        verbose_name = "کتاب الکترونیکی"
        verbose_name_plural = "کتب الکترونیکی"

    def __str__(self) -> str:
        return self.title

    def show_platform(self):
        if self.platform:
            return self.get_platform_display()
        else:
            return '-'

    def get_absolute_url(self):
        return reverse('book:electronicbook')


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
        ('U', "شنیده نشده"), # unheard
        ('L', "در حال شنیدن"), # listening
        ('H', "شنیده شده"), # heard
        ('M', "نشان شده"), # mark
    )
    teller = models.ManyToManyField(Teller, blank=True, verbose_name="گوینده")
    episode = models.PositiveSmallIntegerField(null= True, blank=True, verbose_name="قسمت")
    season = models.PositiveSmallIntegerField(null= True, blank=True, verbose_name="فصل")
    listen_status = models.CharField(max_length=1, choices=LISTEN_STATUS, default='U', verbose_name="وضعیت")
    platform = models.CharField(max_length=5, choices=PLATFROM_LIST, null=True, blank=True, verbose_name="منبع کتاب")
    book_file = models.FileField(upload_to='audiobook_files/', null=True, blank=True, validators=[audiobook_file_format_validator])

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

    def show_platform(self):
        if self.platform:
            return self.get_platform_display()
        else:
            return '-'

    def get_absolute_url(self):
        return reverse('book:audiobook')