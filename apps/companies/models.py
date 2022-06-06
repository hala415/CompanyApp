#import imp
from lib2to3.pytree import Base
from django.db import models
from django.utils.translation import gettext_lazy as _
from CompanyApp.models import BaseModel
#Create your models here.

class Company(BaseModel):
   company_name = models.CharField(_("company name"), max_length=50)

   def __str__(self):
      return self.company_name


   class Meta:
         verbose_name = _("Company")
         verbose_name_plural = _("Companies")


