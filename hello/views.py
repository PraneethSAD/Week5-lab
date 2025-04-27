from django.http import JsonResponse
from django.shortcuts import render

def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})
# Create your views here.
