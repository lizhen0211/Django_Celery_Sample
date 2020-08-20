from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django_celery.tasks import receivedata
from utils.responses import HttpJsonResponse


class CeleryView(View):
    def get(self, request):
        print(request)
        result = receivedata.delay(1, 2)
        #add.apply_async((2, 2))
        print(result)
        return HttpJsonResponse(status=204)
