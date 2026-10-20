from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    location = models.CharField(
        max_length=30
    )

    manager = models.ForeignKey(
        'employees.Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_departments'
    )

    email_address = models.EmailField(
        unique=True
    )

    phone_number = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('departments:department-detail', kwargs={'pk': self.pk})