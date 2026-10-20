from django.urls import path

from employees.views import EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, EmployeeListView, \
    EmployeeDetailView

app_name = 'employees'

urlpatterns = [
    path('create/', EmployeeCreateView.as_view(), name='create'),
    path('edit/<slug:slug>/<int:pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('delete/<slug:slug>/<int:pk>/', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('list/', EmployeeListView.as_view(), name='employees-list' ),
    path('<slug:slug>/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail')
]