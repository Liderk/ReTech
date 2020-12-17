from django.contrib import admin

from .models import Account, Company, Task


@admin.register(Company)
class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


@admin.register(Task)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'task', 'company')
    search_fields = ('name',)
    empty_value_display = 'None'


@admin.register(Account)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'company_access')
