from django.conf.urls import url

from .controllers import *

urlpatterns = [
    url(r'^$', PingController.as_view()),
]
