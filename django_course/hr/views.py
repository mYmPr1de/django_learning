from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView
)

from .forms import EmployeeForm
from .models import Employee


def user_is_superadmin(user) -> bool:
    return user.is_superuser


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')

        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(position__title__icontains=search),
            )
        return queryset


class EmployeeCreateView(UserPassesTestMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return user_is_superadmin(self.request.user)


class EmployeeUpdateView(UserPassesTestMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return user_is_superadmin(self.request.user)


class EmployeeDeleteView(UserPassesTestMixin, DeleteView):
    model = Employee
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return user_is_superadmin(self.request.user)