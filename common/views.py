from django.db.models import Sum, Avg
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

    projects_budget = ProjectRecords.objects.aggregate(
        Sum('allocated_budget'))['allocated_budget__sum']

    departments_budget = DepartmentRecords.objects.aggregate(
        Sum('annual_budget'))['annual_budget__sum']

    bonus_eligibility_count = EmployeeRecords.objects.filter(bonus_eligibility=True).count()

    active_projects_count = ProjectRecords.objects.filter(status='Ongoing').count()

    avg_project_completion = round(
        ProjectRecords.objects.aggregate(Avg('completion_percentage'))['completion_percentage__avg'])

    avg_salary = round(
        EmployeeRecords.objects.aggregate(Avg('salary'))['salary__avg'])

    avg_sick_leave = round(
        EmployeeRecords.objects.aggregate(Avg('sick_leave_days'))['sick_leave_days__avg']
    )

    avg_paid_leave = round(
        EmployeeRecords.objects.aggregate(Avg('paid_leave_allowance'))['paid_leave_allowance__avg']
    )


    context = {
        'employee_count': Employee.objects.count(),
        'projects_count': Project.objects.count(),
        'departments_count': Department.objects.count(),
        'records_count': total_records,
        'active_projects_count': active_projects_count,
        'bonus_eligibility_count': bonus_eligibility_count,
        'projects_budget': projects_budget,
        'departments_budget': departments_budget,
        'average_project_completion': avg_project_completion,
        'average_sick_leave': avg_sick_leave,
        'average_paid_leave': avg_paid_leave,
        'average_salary': avg_salary


    }

    return render(request, 'common/homepage.html', context)

