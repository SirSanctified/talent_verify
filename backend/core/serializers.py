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
