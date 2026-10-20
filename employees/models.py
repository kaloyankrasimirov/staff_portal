from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Employee(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    job_title = models.CharField(
        max_length=50,
    )

    email_address = models.EmailField(
        unique=True,
    )

    phone_number = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name = 'subordinates',
    )

    date_of_hire = models.DateField(
        auto_now_add=True
    )

    department = models.ForeignKey(
        'departments.Department',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name = 'employees'
    )

    slug = models.CharField(
        max_length=100,
        blank=True,
        editable=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name}-{self.last_name}')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('employees:employee-detail', kwargs={'slug': self.slug, 'pk': self.pk})