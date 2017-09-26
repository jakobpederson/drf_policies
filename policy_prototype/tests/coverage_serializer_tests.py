import simplejson as json
from django import test
from rest_framework.reverse import reverse
from rest_framework import status

from policy_prototype.models import Policy


class CoverageSerializerTests(test.TestCase):

    def test_can_create_a_coverage(self):
        policy = Policy.objects.create(policy_number='x')
        data = {
            "data": {
                "type": "coverage",
                "id": "1",
                "attributes": {
                    "liability": True
                },
                "relationships": {
                    "policy": {
                        "data": {
                            "type": "Policy",
                            "id": policy.pk
                        }
                    }
                }
            }
        }
        url = reverse('api:coverage-list')
        response = self.client.post(url, data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        from jpprint import jpprint
        expected = {'data': {'rabbit': {'policy': {'data': {'type': 'policy', 'id': '1'}}}, 'type': 'coverage', 'attributes': {'liability': True}, 'id': '1'}}
        jpprint(expected, response.json())
        self.assertEqual(expected, response.json())
        self.fail('x')

    def test_validate_coverage_field(self):
        data = {
            "data": {
                "type": "coverage",
                "id": 1,
                "attributes": {
                    "liability": "a" * 11
                }
            }
        }
        url = reverse('api:coverage-list')
        response = self.client.post(url, data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected = 'Ensure this field has no more than 10 characters.'
        self.assertEqual(1, len(response.json()['errors']))
        self.assertEqual(expected, response.json()['errors'][0]['detail'])
