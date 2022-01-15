from tabnanny import verbose
from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=75, null=False, blank=False, verbose_name="نام")
    middle_name = models.CharField(max_length=75, verbose_name="نام میانی")
    last_name = models.CharField(max_length=75, null=False, blank=False, verbose_name="نام خانوادگی")
    avatar = models.ImageField(upload_to='./images/person/', verbose_name="عکس پروفایل")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name


class Category(models.Model):
    title = models.CharField(max_length=150, null=True, verbose_name="دسته‌بندی")
    parent = models.ForeignKey('self', default=True, null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='children', verbose_name='زیردسته')

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"    