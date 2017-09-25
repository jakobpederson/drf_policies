from rest_framework_json_api import serializers, relations
from django.urls import reverse
from policy_prototype.models import Policy, Coverage


class PolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = Policy
        fields = ('policy_number', 'coverages')
        resource_name = 'policy'


class CoverageSerializer(serializers.HyperlinkedModelSerializer):

    policy = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='api:policy-detail')

    included_serializers = {
        "policy": PolicySerializer
    }

    class Meta:
        model = Coverage
        fields = ('liability', 'policy')
        resource_name = 'coverage'

    # def create(self, validated_data):
    #     policy_data = validated_data.pop('policy')
    #     policy = Policy.objects.create(**policy_data)
    #     coverage = Coverage.objects.create(policy=policy, **validated_data)
    #     return coverage

    # def update(self, instance, validated_data):
    #     policy_data = validated_data.pop('policy')
    #     policy, _ = Policy.objects.get_or_create(**policy_data)
    #     for i in validated_data:
    #         attr = getattr(instance, i)
    #         instance.attr = validated_data[i]
    #     instance.policy = policy
    #     instance.save()
    #     return instance
