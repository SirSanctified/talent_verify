"""
This module defines the data models for the Talent Verify application.

Models:
    Company: Represents a company in the system.
    Department: Represents a department in a company.
    Role: Represents a role in a department.
    Employee: Represents an employee in the system.

Each model has fields that represent the properties of the entity. For example, the Company model has fields for the company name, registration number, and address. The Department model has a field for the department name and a foreign key to the Company model. The Role model has a field for the role name and a foreign key to the Department model. The Employee model has fields for the employee name, ID, start date, end date, and a foreign key to the Role model.

The models also have a __str__ method that returns a string representation of the object, typically using one of the object's main identifying fields.
"""

from django.db import models

class Company(models.Model):
    """
    Represents a company in the system.
    """
    company_name = models.SlugField(max_length=255, unique=True, blank=False, null=False, help_text="Enter the name of the company.")
    company_registration_number = models.SlugField(max_length=255, unique=True, blank=False, null=False, help_text="Enter the registration number of the company.")
    company_address = models.TextField(blank=False, null=False, help_text="Enter the address of the company.")

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        """
        Return a string representation of the company object.

        Returns:
            str: The company name.
        """
        return self.company_name


class Department(models.Model):
    """
    Represents a department in the system.
    """
    department_name = models.SlugField(max_length=255, unique=True, blank=False, null=False, help_text="Enter the name of the department.", verbose_name="Department Name", verbose_name_plural="Department Names")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='departments', related_query_name='department', help_text="Select the company for the department.")

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """
        Return a string representation of the department object.

        Returns:
            str: The department name.
        """
        return self.department_name


class Role(models.Model):
    """
    Represents a role in the system.

    Fields:
        role_name (str): The name of the role.
        department (Department): The department to which the role belongs.
    """

    role_name = models.SlugField(max_length=100, primary_key=True, blank=False, null=False, help_text="Enter the name of the role.")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='roles', related_query_name='role', help_text="Select the department for the role.")

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        """
        Returns a string representation of the role object.

        Returns:
            str: The role name.
        """
        return self.role_name


class Employee(models.Model):
    """
    Represents an employee in the system.

    Fields:
        employee_name (CharField): The name of the employee.
        employee_id (CharField): The ID of the employee.
        date_started (DateField): The start date of the employee.
        date_left (DateField): The end date of the employee.
        role_name (ForeignKey): The role of the employee (ForeignKey to the `Role` model).
    """

    employee_name = models.CharField(max_length=100, help_text="Enter the name of the employee")
    employee_id = models.CharField(max_length=100, primary_key=True, help_text="Enter the ID of the employee")
    date_started = models.DateField(blank=False, null=False, help_text="Enter the start date of the employee")
    date_left = models.DateField(help_text="Enter the end date of the employee")
    role_name = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='employees', related_query_name='employee', blank=False, null=False, help_text="Select the role of the employee")

    def __str__(self):
        """
        Returns a string representation of the employee object.

        Returns:
            str: The employee name.
        """
        return self.employee_name
