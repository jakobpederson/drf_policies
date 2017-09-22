from django.conf.urls import url, include
from rest_framework import routers

from policy_prototype import views


# policy_list = views.PolicyViewSet.as_view({
#     'get': 'list',
# })


# urlpatterns = [
#     url(r'^policy/$', policy_list, name='policy_list')
# ]

# def print_url_pattern_names(patterns):
#     """Print a list of urlpattern and their names"""
#     for pat in patterns:
#         if pat.__class__.__name__ == 'RegexURLResolver':            # load patterns from this RegexURLResolver
#             print_url_pattern_names(pat.url_patterns)
#         elif pat.__class__.__name__ == 'RegexURLPattern':           # load name from this RegexURLPattern
#             if pat.name is not None:
#                 print('[API-URL] {} \t\t\t-> {}'.format(pat.name, pat.regex.pattern))

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

# if settings.DEBUG:
#     print_url_pattern_names(urlpatterns)
