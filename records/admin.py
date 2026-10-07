from django.contrib import admin
from unfold.admin import ModelAdmin

from records.models import EmployeeRecords, ProjectRecords, DepartmentRecords


# Register your models here.
@admin.register(EmployeeRecords)
class EmployeeRecordsAdmin(ModelAdmin):
    list_display = [
        'id',

    ]

@admin.register(ProjectRecords)
class ProjectRecordsAdmin(ModelAdmin):
    list_display = [
        'id',

    ]

@admin.register(DepartmentRecords)
class DepartmentRecordsAdmin(ModelAdmin):
    list_display = [
        'id',
        '__str__'
    ]