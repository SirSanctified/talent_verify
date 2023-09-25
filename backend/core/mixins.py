from typing import Any, List
import json, csv, openpyxl
from rest_framework.response import Response
from rest_framework import status
class BulkUpdateViewSetMixin:
    """
    A mixin that provides functionality for bulk updating objects in a viewset
    """

    def get_serializer(self, *args, **kwargs) -> Any:
        """
        Overrides the get_serializer method of the parent class.
        Checks if the request method is POST and the data is a list.
        If so, sets the many parameter of the serializer to True and
        adds a bulk flag to the context.
        Returns the serializer instance.
        """
        if self.request.method in (status.HTTP_201_CREATED,): # type: ignore
            data = kwargs.get('data', None)
            is_bulk = data.get('is_bulk', False)
            kwargs['many'] = is_bulk
            kwargs['context']['bulk'] = is_bulk
        return super().get_serializer(*args, **kwargs) # type: ignore

    def create(self, request, *args, **kwargs) -> Any:
        """
        Overrides the create method of the parent class.
        Checks if the request data is a list.
        If so, calls the bulk_update method.
        Otherwise, calls the parent method to create a single object.
        """
        if request.data.get('is_bulk', False):
            return self.bulk_update(request)
        return super().create(request, *args, **kwargs) # type: ignore

    def bulk_update(self, request) -> Response:
        """
        Performs the bulk update operation.
        Filters the queryset based on the view's get_queryset method.
        Creates a serializer instance with the filtered queryset and
        the request data.
        Validates the serializer and performs the update operation.
        Returns the updated data as a response.
        """
        queryset = self.filter_queryset(self.get_queryset()) # type: ignore
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(
            queryset,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        if serializer.data is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        self.perform_update(serializer) # type: ignore
        return Response(serializer.data, status=status.HTTP_200_OK)




def handle_json_file(file, serializer_class):
    data = json.load(file)
    serializer = serializer_class(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        raise serializers.ValidationError(serializer.errors)  # type: ignore


def handle_csv_file(file, serializer_class):
    reader = csv.DictReader(file)
    data = list(reader)
    serializer = serializer_class(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        raise serializers.ValidationError(serializer.errors) # type: ignore


def handle_excel_file(file, serializer_class):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.active
    data = []
    headers = None
    for row in sheet.iter_rows(values_only=True): # type: ignore
        if headers is None:
            headers = row
        else:
            data.append(dict(zip(headers, row)))
    serializer = serializer_class(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        raise serializers.ValidationError(serializer.errors) # type: ignore
