from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group as DjangoGroup
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content= models.TextField()
    def __str__(self):
        return self.title


class User(AbstractBaseUser):
    #                              V   "_" ?????
    first_name =  models.CharField(_("first name"), max_length=30)
    last_name =  models.CharField(_("last name"), max_length=30)
    email = models.EmailField(verbose_name=_("email address"), max_length=255, unique=True, null=True, blank=True)
    isstaff =  models.BooleanField(_("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site."))
    isactive =  models.BooleanField(_("active"), default=True, help_text=_("is active"))
