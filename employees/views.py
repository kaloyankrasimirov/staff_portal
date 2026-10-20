from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from employees.forms import EmployeeForm
from employees.models import Employee


class EmployeeListView(ListView):
    model = Employee
    paginate_by = 20
    ordering = ['last_name', 'first_name']


class EmployeeDetailView(DetailView):
    model = Employee

class EmployeeCreateView(SuccessMessageMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    success_message = 'Employee successfully created!'

class EmployeeUpdateView(SuccessMessageMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_message = 'Employee successfully updated'

class EmployeeDeleteView(SuccessMessageMixin, DeleteView):
    model = Employee
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('employees:employees-list')
    success_message = 'Employee successfully deleted.'