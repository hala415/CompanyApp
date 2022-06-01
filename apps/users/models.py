from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager , Group as DjangoGroup
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
# Create your models here.

#class Post(models.Model):
#	author = models.ForeignKey(User, on_delete=models.CASCADE)
#	title = models.CharField(max_length=50)
#	content= models.TextField()
#	def __str__(self):
#		return self.title

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", False)
		extra_fields.setdefault("is_superuser", False)
		return self._create_user(email, password, **extra_fields)

	def create_application_user_with_token(self, **extra_fields):
		user = self.model(**extra_fields)
		user.save(using=self._db)

		# Create token
		token = Token.objects.create(user=user)

		return (token, user)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)

		if extra_fields.get("is_staff") is not True:
			raise ValueError("Superuser must have is_staff=True.")
		if extra_fields.get("is_superuser") is not True:
			raise ValueError("Superuser must have is_superuser=True.")

		return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	#                              V   "_" ?????
	first_name =  models.CharField(_("first name"), max_length=30)
	last_name =  models.CharField(_("last name"), max_length=30)
	email = models.EmailField(verbose_name=_("email address"), max_length=255, unique=True, null=True, blank=True)
	is_staff =  models.BooleanField(_("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site."))
	is_active =  models.BooleanField(_("active"), default=True, help_text=_("is active"))
	USERNAME_FIELD = "email"
	RQUIRED_FIELDS = []
	objects = UserManager()
	
	class Meta:
		verbose_name = _("User")
		verbose_name_plural = _("Users")
