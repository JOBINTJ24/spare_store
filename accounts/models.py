from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, fname, lname, phone_number, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not lname:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
                        lname=lname,
                        phone_number=phone_number,
                   

        )

        user.set_password(password)
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.BigIntegerField(default=0)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', 'phone_number']

    objects = MyAccountManager()

    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
