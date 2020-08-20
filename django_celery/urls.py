from django.conf.urls import url

from django_celery.views import CeleryView

urlpatterns = [
    url(r'^web$', CeleryView.as_view()),
]
