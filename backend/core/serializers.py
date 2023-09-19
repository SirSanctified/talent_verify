"""
This module contains serializers for the Company, Department, Role,
and Employee models.

Classes:
    CompanySerializer: Serializes the Company model.
    The fields that are serialized include the URL of the company instance,
    the ID, the company name, the departments within the company,
    the company registration number, and the company address.
    
    DepartmentSerializer: Serializes the Department model.
    The fields that are serialized include the URL of the department instance,
    the ID, the department name, the company to which the department belongs,
    and the roles within the department.
    
    RoleSerializer: Serializes the Role model.
    The fields that are serialized include the URL of the role instance,
    the ID, the role name, the department to which the role belongs,
    the duties associated with the role, and the employees who have this role.
    
    EmployeeSerializer: Serializes the Employee model.
    The fields that are serialized include the URL of the employee instance,
    the ID, the employee name, the employee ID, the date the employee started,
    the date the employee left, and the role name of the employee.
"""


from rest_framework import serializers
from .models import Company, Department, Role, Employee


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes a company object.
    """

    class Meta:
        model = Company
        fields = [
            "url",
            "id",
            "company_name",
            "departments",
            "company_registration_number",
            "company_address",
        ]


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes a department object.
    """

    class Meta:
        model = Department
        fields = ["url", "id", "department_name", "company", "roles"]


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes a role object.
    """

    class Meta:
        model = Role
        fields = ["url", "id", "role_name", "department", "duties", "employees"]


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes an employee object.
    """

    class Meta:
        model = Employee
        fields = [
            "url",
            "id",
            "employee_name",
            "employee_id",
            "date_started",
            "date_left",
            "role_name",
        ]
