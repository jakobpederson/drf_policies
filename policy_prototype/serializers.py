from rest_framework_json_api import serializers, relations
from django.urls import reverse
from policy_prototype.models import Policy, Coverage


class PolicySerializer(serializers.HyperlinkedModelSerializer):
    coverages = serializers.SerializerMethodField('get_link')

    def get_link(self, obj):
        url = "http://localhost:8000/api/coverages/{}/"
        new_list = [url.format(x.pk) for x in obj.coverages.all()]
        return new_list

    class Meta:
        model = Policy
        fields = ('policy_number', 'coverages')


class CoverageSerializer(serializers.HyperlinkedModelSerializer):

    policy = serializers.SerializerMethodField('get_link')

    def get_link(self, obj):
        url = "http://localhost:8000/api/policies/{}/"
        new_list = url.format(obj.policy.id)
        return new_list



    class Meta:
        model = Coverage
        fields = ('liability', 'policy')
