from django.urls import path
from departments.views import DepartmentCreateView, DepartmentListView, DepartmentUpdateView, DepartmentDeleteView, \
    DepartmentDetailView, DepartmentAssignedEmployeesView

app_name = 'departments'

urlpatterns = [
    path('create/', DepartmentCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', DepartmentUpdateView.as_view(), name='department-update'),
    path('delete/<int:pk>/', DepartmentDeleteView.as_view(), name='department-delete'),
    path('list/', DepartmentListView.as_view(), name='departments-list' ),
    path('<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('<int:pk>/assigned-employees/', DepartmentAssignedEmployeesView.as_view(), name='assigned-employees')

]