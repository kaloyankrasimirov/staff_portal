from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from departments.models import Department
from employees.models import Employee
from projects.models import Project
from records.models import EmployeeRecords, ProjectRecords, DepartmentRecords


def home_page_view(request: HttpRequest) -> HttpResponse:

    total_records = (
        EmployeeRecords.objects.count() +
        ProjectRecords.objects.count() +
        DepartmentRecords.objects.count()
    )

    context = {
        'employee_count': Employee.objects.count(),
        'projects_count': Project.objects.count(),
        'departments_count': Department.objects.count(),
        'records_count': total_records
    }

    return render(request, 'common/homepage.html', context)

