from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from frontend.choices import GENDER_CHOICES, STATUS_CHOICES, PRIORITY_CHOICES
from django.conf import settings




class Organisation(models.Model):
    name = models.CharField(max_length=80, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=80, blank=True, default='')
    postcode = models.CharField(max_length=255, blank=True, default='')
    logo = models.ImageField(upload_to='org_image', blank=True, default='')

    def __str__(self):
        return self.name


class Branch(models.Model):
    organisation = models.ForeignKey(Organisation, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=True, default='')
    code = models.CharField(max_length=50, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=80, blank=True, default='')
    postcode = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(max_length=15, blank=True, default='')
    location = models.ForeignKey(Branch, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', blank=True, default='')

    REQUIRED_FIELDS = ['username','first_name','last_name','phone']
    USERNAME_FIELD = 'email'
    
    def get_username(self):
        return self.email


class Department(models.Model):
    name = models.CharField(max_length=80, blank=True, default='')

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    postcode = models.CharField(max_length=10, blank=True, default='')
    phone = models.CharField(max_length=15, blank=True, default='')


    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, blank=True, default='')
    start_date = models.DateTimeField(null=True, default=timezone.now)
    due_date = models.DateTimeField(null=True, default=timezone.now)
    status = models.CharField(max_length=100, blank=True, default='')
    priority = models.ForeignKey(Priority, null=True, blank=True, on_delete=models.CASCADE)
    parent_id = models.IntegerField(null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    createdOn = models.DateTimeField(default=timezone.now)
    createdBy = models.CharField(max_length=100, blank=True, null=True)
    lastEditOn = models.DateTimeField(null=True, default=timezone.now)
    lastEditBy = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.customer.name



