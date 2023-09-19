"""

"""

from django.db import models

class Company(models.Model):
	"""
	
	"""
    company_name = models.CharField(max_length=100, primary_key=True)
	company_registration_number = models.CharField(max_length=100)
	company_address = models.CharField(max_length=100)

	def __str__(self):
		"""
		Return a string representation of the company object.

		Returns:
		    str: The company name.
		"""
		return self.company_name

class Department(models.Model):
	department_name = models.CharField(max_length=100, primary_key=True)
	company_name = models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		"""
		Return a string representation of the department object.

		Returns:
		    str: The department name.
		"""
		return self.department_name

class Role(models.Model):
	role_name = models.CharField(max_length=100, primary_key=True)
	department_name = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		"""
		Return a string representation of the role object.

		Returns:
		    str: The role name.
		"""
		return self.role_name

class Employee(models.Model):
	employee_name = models.CharField(max_length=100, primary_key=True)
	employee_id = models.CharField(max_length=100)
	date_started = models.DateField()
	date_left = models.DateField()
	role_name = models.ForeignKey(Role, on_delete=models.CASCADE)

	def __str__(self):
		"""
		Return a string representation of the employee object.

		Returns:
		    str: The employee name.
		"""
		return self.employee_name
