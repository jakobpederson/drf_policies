from django.shortcuts import render

from rest_framework import viewsets

from policy_prototype.serializers import PolicySerializer, CoverageSerializer
from policy_prototype.models import Policy, Coverage


class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    # resource_name = 'policy'


class CoverageViewSet(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer

    # def create(self, request):
    #     print('BOOM create')
    #     print(dir(request))
    #     print(request.data)
    #     super().create(request)
