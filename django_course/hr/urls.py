from django.urls import path

from .views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, EmployeesDetailView


urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/', EmployeesDetailView.as_view(), name='employee_profile'),
    path('employees/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
]