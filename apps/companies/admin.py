from django.contrib import admin
from .models import Company

class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company_name',)


admin.site.register(Company, CompaniesAdmin)