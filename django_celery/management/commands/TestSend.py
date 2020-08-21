from time import sleep

from django.core.management import BaseCommand

import json

import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        """一个简单的请求"""
        for i in range(50):
            payload = {'num': str(i)}
            r = requests.get('http://127.0.0.1:8000/celery/web',params=payload)
            print(r.status_code)

        self.stdout.write(self.style.SUCCESS('ok'))
