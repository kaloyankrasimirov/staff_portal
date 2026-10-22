from django.db import models
from django.urls import reverse
from common.models import BaseModel
from employees.models import Employee



class Project(BaseModel):
    name = models.CharField(
        max_length=100,

    )

    description = models.TextField(

    )

    project_participants = models.ManyToManyField(
        'employees.Employee',
        blank=True,
        related_name='projects'
    )

    project_lead = models.ForeignKey(
        'employees.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_projects'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:project-detail', kwargs={'pk': self.pk})