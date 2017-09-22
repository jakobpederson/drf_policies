from django.conf.urls import url, include
from rest_framework import routers

from policy_prototype import views


# policy_list = views.PolicyViewSet.as_view({
#     'get': 'list',
# })


# urlpatterns = [
#     url(r'^policy/$', policy_list, name='policy_list')
# ]

router = routers.DefaultRouter()

router.register(r'policies', views.PolicyViewSet)
router.register(r'coverages', views.CoverageViewSet)

# ROUTES = {
#     'policy': views.PolicyViewSet,
#     'coverage': views.CoverageViewSet
# }
# for key, viewset in ROUTES.items():
#     router.register(key, viewset)


urlpatterns = [
    url(r'^', include(router.urls))
]
