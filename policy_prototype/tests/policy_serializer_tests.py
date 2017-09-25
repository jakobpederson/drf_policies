import simplejson as json
from django import test
from rest_framework.reverse import reverse
from rest_framework import status


class PolicySerializerTests(test.TestCase):

    def test_can_create_a_policy(self):
        data = {
            "data": {
                "type": "policy",
                "id": 1,
                "attributes": {
                    "policy_number": "123abc"
                }
            }
        }
        url = reverse('api:policy-list')
        response = self.client.post(url, data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected = {'data': {'attributes': {'coverages': [], 'policy_number': '123abc'}, 'id': '1', 'type': 'policy'}}
        self.assertEqual(expected, response.json())

    def test_validate_policy_field(self):
        data = {
            "data": {
                "type": "policy",
                "id": 1,
                "attributes": {
                    "policy_number": "a" * 11
                }
            }
        }
        url = reverse('api:policy-list')
        response = self.client.post(url, data=json.dumps(data), content_type='application/vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected = 'Ensure this field has no more than 10 characters.'
        self.assertEqual(1, len(response.json()['errors']))
        self.assertEqual(expected, response.json()['errors'][0]['detail'])
