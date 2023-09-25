import os
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .mixins import (
    handle_csv_file,
    handle_excel_file,
    handle_json_file,
    BulkUpdateViewSetMixin,
)
from .serializers import (
    CompanySerializer,
    DepartmentSerializer,
    RoleSerializer,
    EmployeeSerializer,
)
from .models import Company, Department, Role, Employee


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "company_name",
    ]

    @action(
        detail=False,
        methods=["post", "put", "patch"],
        parser_classes=[FileUploadParser],
    )
    def upload(self, request):
        """
        Handles file uploads.

        This method checks the file type and calls the appropriate handler
        function based on the file extension.
        If the file type is invalid, it returns a response with a status code
        of 400 and a message indicating the invalid file type.
        If there is a validation error during file handling, it returns a
        response with a status code of 400 and the validation error message.
        Otherwise, it returns a response with a status code of 204.

        Args:
            self: The instance of the CompanyViewSet class.
            request: The request object containing the file to be uploaded.

        Returns:
            Response object with a status code of 204 if the file is
            successfully uploaded.
            Response object with a status code of 400 and a message if the
            file type is invalid or there is a validation error.
        """
        file = request.data.get("file")
        if file is None:
            return Response(status.HTTP_400_BAD_REQUEST,{"detail": "File not found"})
        try:
            serializer_class = self.get_serializer_class()
            file_handlers = {
                ".json": handle_json_file,
                ".csv": handle_csv_file,
                ".xlsx": handle_excel_file,
            }
            file_extension = os.path.splitext(file.name)[1]
            handler = file_handlers.get(file_extension)
            if handler is None:
                return Response(status.HTTP_400_BAD_REQUEST, {"detail": "Invalid file type"})
            handler(file, serializer_class)
        except ValidationError as e:
            return Response(status.HTTP_400_BAD_REQUEST, {"detail": str(e)})
        return Response(status.HTTP_204_NO_CONTENT)


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be viewed or edited.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["department_name"]


class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """

    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["role_name"]


class EmployeeViewSet(BulkUpdateViewSetMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "employee_name",
        "employee_id",
        "date_started",
        "date_left",
        "role_name",
    ]

    @action(
        detail=False,
        methods=["post", "put", "patch"],
        parser_classes=[FileUploadParser],
    )
    def upload(self, request):
        """
        Handles file uploads.

        This method checks the file type and calls the appropriate handler
        function based on the file extension.
        If the file type is invalid, it returns a response with a status code
        of 400 and a message indicating the invalid file type.
        If there is a validation error during file handling, it returns a
        response with a status code of 400 and the validation error message.
        Otherwise, it returns a response with a status code of 204.

        Args:
            self: The instance of the EmployeeViewSet class.
            request: The request object containing the file to be uploaded.

        Returns:
            Response object with a status code of 204 if the file is
            successfully uploaded.
            Response object with a status code of 400 and a message if the
            file type is invalid or there is a validation error.
        """
        file = request.data.get("file")
        if file is None:
            return Response(status.HTTP_400_BAD_REQUEST,{"detail": "File not found"})
        try:
            serializer_class = self.get_serializer_class()
            file_handlers = {
                ".json": handle_json_file,
                ".csv": handle_csv_file,
                ".xlsx": handle_excel_file,
            }
            file_extension = os.path.splitext(file.name)[1]
            handler = file_handlers.get(file_extension)
            if handler is None:
                return Response(status.HTTP_400_BAD_REQUEST, {"detail": "Invalid file type"})
            handler(file, serializer_class)
        except ValidationError as e:
            return Response(status.HTTP_400_BAD_REQUEST, {"detail": str(e)})
        return Response(status.HTTP_204_NO_CONTENT)