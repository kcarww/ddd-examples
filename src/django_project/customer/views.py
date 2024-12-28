from django.shortcuts import render
from uuid import UUID
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from django_project.customer.repository import DjangoORMCustomerRepository
from django_project.customer.serializers import CreateCustomerRequestSerializer, CreateCustomerResponseSerializer
from use_cases.customer.create.create_customer_dto import CreateCustomerInput
from use_cases.customer.create.create_customer_use_case import CreateCustomerUseCase

class CustomerViewSet(viewsets.ViewSet):

    def create(self, request: Request) -> Response:
        serializer = CreateCustomerRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        customer_input = CreateCustomerInput(**serializer.validated_data)
        use_case = CreateCustomerUseCase(customer_repository=DjangoORMCustomerRepository())
        output = use_case.execute(customer_input)
        return Response(
            status=status.HTTP_201_CREATED,
            data=CreateCustomerResponseSerializer(instance=output).data
        )
