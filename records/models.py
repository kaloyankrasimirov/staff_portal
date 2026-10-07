from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from common.models import BaseModel


class EmployeeRecords(BaseModel):
    class Meta:
        verbose_name_plural = "Employee Records"
    employee = models.OneToOneField(
        'employees.Employee',
        on_delete=models.CASCADE,
        related_name='record'
    )
    paid_leave_allowance = models.PositiveIntegerField(
        default=20
    )

    sick_leave_days = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    bonus_eligibility = models.BooleanField(
        default=False
    )

    manager_review = models.TextField()

    def __str__(self) -> str:
        return f"{self.employee.first_name} {self.employee.last_name}'s archive"



class ProjectRecords(BaseModel):
    class Meta:
        verbose_name_plural = "Project Records"

    class StatusChoices(models.TextChoices):
        COMPLETED = 'Completed', 'Completed',
        NOT_STARTED = 'Not-Started', 'Not-Started',
        ONGOING = 'Ongoing', 'Ongoing',
        ON_HOLD = 'On-hold', 'On-hold',
        CANCELLED = 'Cancelled', 'Cancelled',

    project = models.OneToOneField(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='record'
    )

    allocated_budget = models.IntegerField()

    milestones = models.TextField(
        blank=True,
        null=True
    )
    targets = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.NOT_STARTED
    )

    completion_percentage = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )

    def clean(self):
        super().clean()
        if self.status == self.StatusChoices.ONGOING and self.completion_percentage is None:
            raise ValidationError({
                'completion_percentage': 'Completion percentage is a required field.'
            })

    def __str__(self) -> str:
        return f"{self.project}'s archive"


class DepartmentRecords(BaseModel):
    class Meta:
        verbose_name_plural = "Department Records"

    department = models.OneToOneField(
        'departments.Department',
        on_delete=models.CASCADE,
        related_name='record'
    )
    annual_budget = models.PositiveIntegerField()

    headcount_target = models.PositiveIntegerField()

    strategic_goals = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.department}'s archive"
