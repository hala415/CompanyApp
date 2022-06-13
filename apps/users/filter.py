from attr import fields
from platformdirs import user_cache_dir
import django_filters
from .models import User

class UserFilter(django_filters.FilterSet):

   class Meta:
      model = User
      fields= ('first_name', 'last_name', 'email')
