from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import (
    Department,
    Employee,
    Position,
    Company
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_department')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'tax_code')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'is_manager')

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            form.add_error(None, e)
            super().save_model(request, obj, form, change)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'position', 'hire_date', 'phone_number')
