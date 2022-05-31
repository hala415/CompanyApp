from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
	#                                                                  V      ????           
	create_date = models.DateTimeField(auto_now_add=True, verbose_name=_("create date"), null=True)
	update_date = models.DateTimeField(auto_now=True, verbose_name=_("update date"), null=True)
	
	class Meta:
		abstract = True