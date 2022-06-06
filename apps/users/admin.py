from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    #fieldsets = {'First Name': ('first_name'), 'Last Name': ('last_name'), 'Email': ('email'), }


    
admin.site.unregister(Group)

admin.site.register(User, UsersAdmin)


#(('standard info', {'fields': ('name',)}), ('Adress info', {'fields': ('address', ('city', 'zipp'),)}),)