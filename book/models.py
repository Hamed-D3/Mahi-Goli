from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=75, null=False, blank=False)
    middle_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75, null=False, blank=False)
    avatar = models.ImageField(upload_to='/images/person/')

    def __str__(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name


class Category(models.Model):
    title = models.CharField(max_length=150)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL)