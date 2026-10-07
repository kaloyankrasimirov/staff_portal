from django.contrib import admin
from unfold.admin import ModelAdmin

from projects.models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = [
        'id',
        'name',
    ]