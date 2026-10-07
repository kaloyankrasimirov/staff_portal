from django.contrib import admin
from unfold.admin import ModelAdmin

from departments.models import Department


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(ModelAdmin):
    list_display = [
        'id',
        'name',
        'internal_code',
        'location',
        'manager',
        'email_address',
        'phone_number',
        ]