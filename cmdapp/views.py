from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from cmdapp.serializer import *
from cmdapp.models import *

class EmpOperations(ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

class AddressOperations(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    