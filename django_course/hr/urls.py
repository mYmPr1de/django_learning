from django.urls import path

from .views import EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView


urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
]