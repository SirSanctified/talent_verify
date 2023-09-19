"""
This module sets up the API routing for the application.

It imports the necessary modules and viewsets from Django Rest Framework and the local views module. 
Then, it creates a default router and registers the viewsets with their respective endpoints.

Imports:
    routers from rest_framework: DefaultRouter class to set up the API routes.
    CompanyViewSet, DepartmentViewSet, RoleViewSet, EmployeeViewSet from local views module: ViewSets for each model in the application.

Variables:
    router: DefaultRouter instance where the viewsets are registered.

API Routes:
    /companies: Endpoint for viewing and editing Company instances.
    /departments: Endpoint for viewing and editing Department instances.
    /roles: Endpoint for viewing and editing Role instances.
    /employees: Endpoint for viewing and editing Employee instances.
"""
from rest_framework import routers
from .views import (
    CompanyViewSet,
    DepartmentViewSet,
    RoleViewSet,
    EmployeeViewSet,
)

router = routers.DefaultRouter()

router.register(r"companies", CompanyViewSet)
router.register(r"departments", DepartmentViewSet)
router.register(r"roles", RoleViewSet)
router.register(r"employees", EmployeeViewSet)