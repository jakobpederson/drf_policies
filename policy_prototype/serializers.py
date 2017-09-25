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

    def id(self, obj):
        url = "http://localhost:8000/api/policies/{}/"
        new_list = url.format(obj.policy.id)
        return new_list


class CoverageSerializer(serializers.HyperlinkedModelSerializer):

    policy = PolicySerializer()

    class Meta:
        model = Coverage
        fields = ('liability', 'policy')

    def create(self, validated_data):
        policy_data = validated_data.pop('policy')
        policy = Policy.objects.create(**policy_data)
        coverage = Coverage.objects.create(policy=policy, **validated_data)
        return coverage

    def update(self, instance, validated_data):
        policy_data = validated_data.pop('policy')
        policy, _ = Policy.objects.get_or_create(**policy_data)
        for i in validated_data:
            attr = getattr(instance, i)
            instance.attr = validated_data[i]
        instance.policy = policy
        instance.save()
        return instance
