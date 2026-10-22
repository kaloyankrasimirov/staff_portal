from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from common.forms import SearchForm
from employees.forms import EmployeeForm
from employees.models import Employee


class EmployeeListView(ListView):
    model = Employee
    paginate_by = 10
    ordering = ['first_name', 'last_name']

    def get_queryset(self):
        qs = super().get_queryset()
        self.search_form = SearchForm(self.request.GET or None)

        if self.search_form.is_valid():
            query = self.search_form.cleaned_data.get('query')
            if query:
                qs = (qs.filter(first_name__icontains=query) |
                      qs.filter(last_name__icontains=query))

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context

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