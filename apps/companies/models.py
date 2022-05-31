from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Company():
    company_name = models.CharField(_("company name"), max_length=50)
 