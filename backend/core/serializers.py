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
from rest_framework.fields import empty
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
        extra_kwargs = {
            "company_registration_number": {"required": True},
            "company_address": {"required": True},
            "departments": {"required": False},
        }


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes a department object.
    """

    def __init__(self, instance=None, data=empty, **kwargs):
        if instance:
            setattr(self.Meta, "depth", 1)
        else:
            setattr(self.Meta, "depth", 0)
        super(DepartmentSerializer, self).__init__(instance, data, **kwargs)

    class Meta:
        model = Department
        depth = 1
        fields = ["url", "id", "department_name", "company", "roles"]
        extra_kwargs = {"roles": {"required": False}}


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes a role object.
    """

    def __init__(self, instance=None, data=empty, **kwargs):
        if instance:
            setattr(self.Meta, "depth", 1)
        else:
            setattr(self.Meta, "depth", 0)
        super(RoleSerializer, self).__init__(instance, data, **kwargs)

    class Meta:
        model = Role
        depth = 1
        fields = [
            "url",
            "id",
            "role_name",
            "department",
            "duties",
            "employees",
        ]
        extra_kwargs = {"duties": {"required": False}, "employees": {"required": False}}


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes an employee object.
    """

    def __init__(self, instance=None, data=empty, **kwargs):
        if instance:
            setattr(self.Meta, "depth", 1)
        else:
            setattr(self.Meta, "depth", 0)
        super(EmployeeSerializer, self).__init__(instance, data, **kwargs)

    class Meta:
        model = Employee
        depth = 1
        fields = [
            "url",
            "id",
            "employee_name",
            "employee_id",
            "date_started",
            "date_left",
            "role",
        ]
        extra_kwargs = {
            "employee_id": {"required": True},
            "date_started": {"required": True},
            "role": {"required": False},
        }
