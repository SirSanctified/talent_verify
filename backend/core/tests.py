from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company, Department, Role, Employee
from .serializers import (
    CompanySerializer,
    DepartmentSerializer,
    RoleSerializer,
    EmployeeSerializer,
)


class CompanyTests(APITestCase):
    def test_create_company(self):
        """
        Ensure we can create a new company object.
        """
        url = reverse("company-list")
        data = {"company_name": "test_company", "company_registration_number": "test_company_registration_number", "company_address": "test_company_address"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().company_name, "test_company")

    def test_get_company(self):
        """
        Ensure we can get a company object.
        """
        company = Company.objects.create(company_name="test_company", company_registration_number="test_company_registration_number", company_address="test_company_address")
        url = reverse("company-detail", kwargs={"pk": company.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["company_name"], "test_company") # type: ignore

    def test_update_company(self):
        """
        Ensure we can update a company object.
        """
        company = Company.objects.create(company_name="test_company", company_registration_number="test_company_registration_number", company_address="test_company_address")
        url = reverse("company-detail", kwargs={"pk": company.pk})
        data = {"company_name": "test_company_updated"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.content, b'{"url":"http://testserver/companies/1/","id":1,"company_name":"test_company_updated","departments":[],"company_registration_number":"test_company_registration_number","company_address":"test_company_address"}'
        )

    def test_delete_company(self):
        """
        Ensure we can delete a company object.
        """
        company = Company.objects.create(company_name="test_company", company_registration_number="test_company_registration_number", company_address="test_company_address")
        url = reverse("company-detail", kwargs={"pk": company.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.count(), 0)

    def test_search_company(self):
        """
        Ensure we can search a company object.
        """
        company = Company.objects.create(company_name="test_company", company_registration_number="test_company_registration_number", company_address="test_company_address")
        url = reverse("company-list")
        response = self.client.get(url, {"search": "test_company"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'[{"url":"http://testserver/companies/1/","id":1,"company_name":"test_company","departments":[],"company_registration_number":"test_company_registration_number","company_address":"test_company_address"}]')

    def test_search_company_no_results(self):
        """
        Ensure we can search a company object with no results.
        """
        company = Company.objects.create(company_name="test_company", company_registration_number="test_company_registration_number", company_address="test_company_address")
        url = reverse("company-list")
        response = self.client.get(url, {"search": "test_company_no_results"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, b'[]')


class DepartmentTests(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(company_name="test_company", company_registration_number="test_company_registration_number", company_address="test_company_address")

    def test_create_department(self):
        """
        Ensure we can create a new department object.
        """
        url = reverse("department-list")
        data = {"department_name": "test_department", "company": "http://testserver/companies/1/"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 1)
        self.assertEqual(Department.objects.get().department_name, "test_department")

    def test_get_department(self):
        """
        Ensure we can get a department object.
        """
        department = Department.objects.create(
            department_name="test_department", company=self.company
        )
        url = reverse("department-detail", kwargs={"pk": department.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["department_name"], "test_department" # type: ignore
        )

    def test_update_department(self):
        """
        Ensure we can update a department object.
        """
        department = Department.objects.create(
            department_name="test_department", company=self.company
        )
        url = reverse("department-detail", kwargs={"pk": department.pk})
        data = {"department_name": "test_department_updated"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["department_name"], "test_department_updated" # type: ignore
        )

    def test_delete_department(self):
        """
        Ensure we can delete a department object.
        """
        department = Department.objects.create(
            department_name="test_department", company=self.company
        )
        url = reverse("department-detail", kwargs={"pk": department.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), 0)

    def test_search_department(self):
        """
        Ensure we can search a department object.
        """
        department = Department.objects.create(
            department_name="test_department", company=self.company
        )
        url = reverse("department-list")
        response = self.client.get(url, {"search": "test_department"})
        self.assertEqual(response.content, b'[{"url":"http://testserver/departments/1/","id":1,"department_name":"test_department","company":{"url":"http://testserver/companies/1/","company_name":"test_company","company_registration_number":"test_company_registration_number","company_address":"test_company_address"},"roles":[]}]')

    def test_search_department_no_results(self):
        """
        Ensure we can search a department object with no results.
        """
        department = Department.objects.create(
            department_name="test_department", company=self.company
        )
        url = reverse("department-list")
        response = self.client.get(url, {"search": "test_department_no_results"})
        self.assertEqual(response.content, b'[]')


class RoleTests(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(company_name="test_company", company_registration_number="test_company_registration_number", company_address="test_company_address")
        self.department = Department.objects.create(
            department_name="test_department", company=self.company
        )
    
    def test_create_role(self):
        """
        Ensure we can create a new role object.
        """
        url = reverse("role-list")
        data = {"role_name": "test_role", "department": "http://testserver/departments/1/", "duties": "test_duties"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Role.objects.count(), 1)
        self.assertEqual(Role.objects.get().role_name, "test_role")
    
    def test_get_role(self):
        """
        Ensure we can get a role object.
        """
        role = Role.objects.create(
            role_name="test_role", department=self.department, duties="test_duties"
        )
        url = reverse("role-detail", kwargs={"pk": role.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["role_name"], "test_role" # type: ignore
        )
    
    def test_update_role(self):
        """
        Ensure we can update a role object.
        """
        role = Role.objects.create(
            role_name="test_role", department=self.department, duties="test_duties"
        )
        url = reverse("role-detail", kwargs={"pk": role.pk})
        data = {"role_name": "test_role_updated"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["role_name"], "test_role_updated" # type: ignore
        )
    
    def test_delete_role(self):
        """
        Ensure we can delete a role object.
        """
        role = Role.objects.create(
            role_name="test_role", department=self.department, duties="test_duties"
        )
        url = reverse("role-detail", kwargs={"pk": role.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Role.objects.count(), 0)
    
    def test_search_role(self):
        """
        Ensure we can search a role object.
        """
        role = Role.objects.create(
            role_name="test_role", department=self.department, duties="test_duties"
        )
        url = reverse("role-list")
        response = self.client.get(url, {"search": "test_role"})
        self.assertEqual(response.content, b'[{"url":"http://testserver/roles/1/","id":1,"role_name":"test_role","department":{"url":"http://testserver/departments/1/","department_name":"test_department","company":"http://testserver/companies/1/"},"duties":"test_duties","employees":[]}]')

    def test_search_role_no_results(self):
        """
        Ensure we can search a role object with no results.
        """
        role = Role.objects.create(
            role_name="test_role", department=self.department, duties="test_duties"
        )
        url = reverse("role-list")
        response = self.client.get(url, {"search": "test_role_no_results"})
        self.assertNotEqual(response.content, b'{"count":0,"next":null,"previous":null,"results":[]}')
    

class EmployeeTests(APITestCase):
    def setUp(self):
        self.company = Company.objects.create(company_name="test_company", company_registration_number="test_company_registration_number", company_address="test_company_address")
        self.department = Department.objects.create(
            department_name="test_department", company=self.company
        )
        self.role = Role.objects.create(
            role_name="test_role", department=self.department, duties="test_duties"
        )

    def test_create_employee(self):
        """
        Ensure we can create a new employee object.
        """
        url = reverse("employee-list")
        data = {"employee_name": "test_employee", "employee_id": "test_employee_id", "role": "http://testserver/roles/1/", "date_started": "2021-01-01", "date_left": "2021-01-01"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().employee_name, "test_employee")

    def test_get_employee(self):
        """
        Ensure we can get a employee object.
        """
        employee = Employee.objects.create(
            employee_name="test_employee", employee_id="test_employee_id", role=self.role, date_started="2021-01-01", date_left="2021-01-01"
        )
        url = reverse("employee-detail", kwargs={"pk": employee.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["employee_name"], "test_employee" # type: ignore
        )

    def test_update_employee(self):
        """
        Ensure we can update a employee object.
        """
        employee = Employee.objects.create(
            employee_name="test_employee", employee_id="test_employee_id", role=self.role, date_started="2021-01-01", date_left="2021-01-01"
        )
        url = reverse("employee-detail", kwargs={"pk": employee.pk})
        data = {"employee_name": "test_employee_updated"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["employee_name"], "test_employee_updated" # type: ignore
        )

    def test_delete_employee(self):
        """
        Ensure we can delete a employee object.
        """
        employee = Employee.objects.create(
            employee_name="test_employee", employee_id="test_employee_id", role=self.role, date_started="2021-01-01", date_left="2021-01-01"
        )
        url = reverse("employee-detail", kwargs={"pk": employee.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)
    
    def test_search_employee(self):
        """
        Ensure we can search a employee object.
        """
        employee = Employee.objects.create(
            employee_name="test_employee", employee_id="test_employee_id", role=self.role, date_started="2021-01-01", date_left="2021-01-01"
        )
        url = reverse("employee-list")
        response = self.client.get(url, {"query": "test_employee"})
        self.assertEqual(response.content, b'[{"url":"http://testserver/employees/1/","id":1,"employee_name":"test_employee","employee_id":"test_employee_id","date_started":"2021-01-01","date_left":"2021-01-01","role":{"url":"http://testserver/roles/1/","role_name":"test_role","duties":"test_duties","department":"http://testserver/departments/1/"}}]')

    def test_search_employee_no_results(self):
        """
        Ensure we can search a employee object with no results.
        """
        employee = Employee.objects.create(
            employee_name="test_employee", employee_id="test_employee_id", role=self.role, date_started="2021-01-01", date_left="2021-01-01"
        )
        url = reverse("employee-list")
        response = self.client.get(url, {"query": "test_employee_no_results"})
        self.assertEqual(response.content, b'[]')
    
