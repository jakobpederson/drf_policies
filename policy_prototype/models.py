from django.db import models


class Policy(models.Model):

    policy_number = models.CharField(max_length=10)

    class Meta:
        ordering = ('policy_number',)

    class JSONAPIMeta:
        related_name = 'policy'

    def __str__(self):
        return self.policy_number


class Coverage(models.Model):
    liability = models.BooleanField(default=False)
    policy = models.ForeignKey(Policy, related_name='coverages')

    class JSONAPIMeta:
        related_name = 'coverage'

    def __str__(self):
        return 'Coverage for {}'.format(self.policy.policy_number)
