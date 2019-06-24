from django.conf.urls import url

from .controllers import *

urlpatterns = [
    url(r'^$', HierarchyController.as_view()),
]
