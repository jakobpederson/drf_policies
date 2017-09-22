from rest_framework_json_api import serializers, relations
from policy_prototype.models import Policy, Coverage


class PolicySerializer(serializers.HyperlinkedModelSerializer):
    coverages = relations.ResourceRelatedField(read_only=True, many=True)

    # coverages = relations.HyperlinkedRelatedField(
    #     read_only=True,
    #     many=True,
    #     view_name='coverages',
    #     lookup_field='',
    # )

    class Meta:
        model = Policy
        fields = ('policy_number', 'coverages')


class CoverageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Coverage
        fields = ('liability', 'policy')
