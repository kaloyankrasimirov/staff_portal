
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('departments/', include('departments.urls')),
    path('employees/', include('employees.urls')),
    path('projects/', include('projects.urls')),
    path('records/', include('records.urls'))

]
