from django.urls import path

from projects.views import ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectListView, ProjectDetailView, \
    ProjectAssignedEmployeesView

app_name = 'projects'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ProjectUpdateView.as_view(), name='project-update'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='project-delete'),
    path('list/', ProjectListView.as_view(), name='projects-list' ),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/assigned-employees/', ProjectAssignedEmployeesView.as_view(), name='assigned-employees')

]