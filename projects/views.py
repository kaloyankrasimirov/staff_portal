from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from common.forms import SearchForm
from employees.models import Employee
from projects.forms import ProjectForm
from projects.models import Project


class ProjectListView(ListView):
    model = Project
    paginate_by = 5
    ordering = 'name'

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


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView, SuccessMessageMixin):
    model = Project
    form_class = ProjectForm
    success_message = 'Project successfully created!'


class ProjectUpdateView(SuccessMessageMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    success_message = 'Project successfully updated!'

class ProjectDeleteView(SuccessMessageMixin, DeleteView):
    model = Project
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('projects:projects-list')
    success_message = 'Project successfully deleted.'


class ProjectAssignedEmployeesView(ListView):
    model = Project
    template_name = 'projects/project_assigned_employees.html'
    paginate_by = 10


    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk')
        project = Project.objects.get(pk=pk)
        qs = project.project_participants.all().order_by('first_name', 'last_name')

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        context['project'] = project

        return context