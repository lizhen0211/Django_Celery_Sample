from time import sleep

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django_celery.tasks import receivedata
from utils.responses import HttpJsonResponse


class CeleryView(View):
    def get(self, request):
        print(request)
        param = request.GET.get('num')
        print(param)
        # result = receivedata.delay(param)
        result = receivedata.delay(param)
        # result = receivedata.apply_async((param,), queue='receivedata_queue')
        print("view:"+str(result.ready()))
        # print("view:" + str(result.get()))
        return HttpJsonResponse(status=204)
