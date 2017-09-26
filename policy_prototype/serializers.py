from rest_framework_json_api import serializers, relations
from django.urls import reverse
from policy_prototype.models import Policy, Coverage


class PolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = Policy
        fields = ('policy_number', 'coverages')
        resource_name = 'policy'


class CoverageSerializer(serializers.ModelSerializer):

    policy =  PolicySerializer

    class Meta:
        model = Coverage
        fields = ('liability', 'policy')
        resource_name = 'coverage'
