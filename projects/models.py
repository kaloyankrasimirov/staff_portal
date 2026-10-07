from django.db import models

from common.models import BaseModel
from employees.models import Employee



class Project(BaseModel):
    name = models.CharField(
        max_length=100,

    )

    description = models.TextField(

    )

    project_participants = models.ManyToManyField(
        Employee,
        related_name='projects'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name