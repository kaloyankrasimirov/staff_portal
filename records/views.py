from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from records.forms import EmployeeRecordsForm, DepartmentRecordsForm, ProjectRecordsForm
from records.models import EmployeeRecords, ProjectRecords, DepartmentRecords

class RecordsDashboardView(TemplateView):
    template_name = 'records/records_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_records'] = EmployeeRecords.objects.select_related('employee').all()
        context['project_records'] = ProjectRecords.objects.select_related('project').all()
        context['department_records'] = DepartmentRecords.objects.select_related('department').all()
        return context


class EmployeeRecordsCreateView(CreateView, SuccessMessageMixin):
    model = EmployeeRecords
    form_class = EmployeeRecordsForm
    success_url = reverse_lazy('records:records-dashboard')
    success_message = 'Employee record successfully created!'


class EmployeeRecordsUpdateView(UpdateView, SuccessMessageMixin):
    model = EmployeeRecords
    form_class = EmployeeRecordsForm
    success_url = reverse_lazy('records:records-dashboard')
    success_message = 'Employee record successfully updated!'

class DepartmentRecordsCreateView(CreateView, SuccessMessageMixin):
    model = DepartmentRecords
    form_class = DepartmentRecordsForm
    success_url = reverse_lazy('records:records-dashboard')
    success_message = 'Department record successfully created!'

class DepartmentRecordsUpdateView(UpdateView, SuccessMessageMixin):
    model = DepartmentRecords
    form_class = DepartmentRecordsForm
    success_url = reverse_lazy('records:records-dashboard')
    success_message = 'Department record successfully updated!'

class ProjectRecordsCreateView(CreateView, SuccessMessageMixin):
    model = ProjectRecords
    form_class = ProjectRecordsForm
    success_url = reverse_lazy('records:records-dashboard')
    success_message = 'Project record successfully created!'

class ProjectRecordsUpdateView(UpdateView, SuccessMessageMixin):
    model = ProjectRecords
    form_class = ProjectRecordsForm
    success_url = reverse_lazy('records:records-dashboard')
    success_message = 'Project record successfully updated!'