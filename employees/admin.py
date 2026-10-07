from django.contrib import admin
from unfold.admin import ModelAdmin

from employees.models import Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'job_title',
        'department',
        'manager',
        'date_of_hire',
        'email_address',
        'phone_number',
    ]