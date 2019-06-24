from django.conf.urls import url, include

import api_commons.common

urlpatterns = [
    url(r'^ping/?', include('api.ping.urls')),
    url(r'^calc/?', include('api.calculator.urls')),
    url(r'^hierarchy/?', include('api.hierarchy.urls')),
]

handler404 = api_commons.common.error_404_handler
handler500 = api_commons.common.error_500_handler
