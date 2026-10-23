from django.urls import path

from records.views import RecordsDashboardView, EmployeeRecordsCreateView, EmployeeRecordsUpdateView, \
    DepartmentRecordsCreateView, DepartmentRecordsUpdateView, ProjectRecordsCreateView, ProjectRecordsUpdateView

app_name = 'records'

urlpatterns = [
    path('', RecordsDashboardView.as_view(), name='records-dashboard'),
    path('employee/create/', EmployeeRecordsCreateView.as_view(), name='employee-record-create'),
    path('records/', EmployeeRecordsUpdateView.as_view(), name='employee-record-update'),
    path('deparment/create/', DepartmentRecordsCreateView.as_view(), name='department-record-create'),
    path('records/', DepartmentRecordsUpdateView.as_view(), name='department-record-update'),
    path('project/create/', ProjectRecordsCreateView.as_view(), name='project-record-create'),
    path('records/', ProjectRecordsUpdateView.as_view(), name='project-record-update'),
]