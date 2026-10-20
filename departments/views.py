from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from departments.forms import DepartmentForm
from departments.models import Department


class DepartmentListView(ListView):
    model = Department
    paginate_by = 5
    ordering = ['-name']


class DepartmentDetailView(DetailView):
    model = Department


class DepartmentCreateView(SuccessMessageMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    success_message = 'Department successfully created!'


class DepartmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    success_message = 'Department successfully updated!'

class DepartmentDeleteView(SuccessMessageMixin, DeleteView):
    model = Department
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('departments:departments-list')
    success_message = 'Department successfully deleted.'