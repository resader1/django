from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers # json타입
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def list(request):
    return HttpResponse('데이터전달')