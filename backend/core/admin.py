from django.contrib import admin
from .models import Company, Department, Employee, Role


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_name", "company_registration_number", "company_address")
    list_filter = ("company_name", "company_registration_number")
    search_fields = ("company_name", "company_registration_number")
    ordering = ("company_name", "company_registration_number")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_name", "company")
    list_filter = ("department_name", "company")
    search_fields = ("department_name", "company")
    ordering = ("department_name", "company")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("role_name", "department")
    list_filter = ("role_name", "department")
    search_fields = ("role_name", "department")
    ordering = ("role_name", "department")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_name",
        "employee_id",
        "date_started",
        "date_left",
    )
    list_filter = (
        "employee_name",
        "employee_id",
        "date_started",
        "date_left",
    )
    search_fields = (
        "employee_name",
        "employee_id",
        "date_started",
        "date_left",
    )
    ordering = (
        "employee_name",
        "employee_id",
        "date_started",
        "date_left",
    )
