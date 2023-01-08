from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import *
from myapp.serializers import ContactSerializer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.myapp

@csrf_exempt

def api_list(request):
  if request.method == "GET":
    api_data =Contact.objects.all()
    serializer = ContactSerializer(api_data,many=True)
    return JsonResponse(serializer.data, safe=False)
  
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = ContactSerializer(data =data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status = 201)
    return JsonResponse(serializer.errors, status = 400)
  
  

@csrf_exempt
def api_detail(request, pk):
    
    try:
        api_details = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContactSerializer(api_details)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(api_details, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        api_details.delete()