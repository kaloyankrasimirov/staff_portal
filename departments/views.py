from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from departments.forms import DepartmentForm
from departments.models import Department
from employees.models import Employee
from common.forms import SearchForm


class DepartmentListView(ListView):
    model = Department
    paginate_by = 5
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        self.search_form = SearchForm(self.request.GET or None)

        if self.search_form.is_valid():
            query = self.search_form.cleaned_data.get('query')
            if query:
                qs = (qs.filter(name__icontains=query))


        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


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

class DepartmentAssignedEmployeesView(ListView):
    model = Employee
    template_name = 'departments/department_assigned_employees.html'
    paginate_by = 10


    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk')
        qs = Employee.objects.filter(department=pk).order_by('first_name', 'last_name')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = Department.objects.get(pk=self.kwargs.get('pk'))
        context['department'] = department

        return context