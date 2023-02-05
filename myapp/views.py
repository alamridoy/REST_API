from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import *
from myapp.serializers import ContactSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.reverse import reverse
from rest_framework import mixins
from rest_framework import generics


#-------------------serializer-------------
# @csrf_exempt

# def api_list(request):
#   if request.method == "GET":
#     api_data =Contact.objects.all()
#     serializer = ContactSerializer(api_data,many=True)
#     return JsonResponse(serializer.data, safe=False)
  
#   elif request.method == 'POST':
#     data = JSONParser().parse(request)
#     serializer = ContactSerializer(data =data)
#     if serializer.is_valid():
#       serializer.save()
#       return JsonResponse(serializer.data, status = 201)
#     return JsonResponse(serializer.errors, status = 400)
  
  

# @csrf_exempt
# def api_detail(request, pk):
    
#     try:
#         api_details = Contact.objects.get(pk=pk)
#     except Contact.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ContactSerializer(api_details)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ContactSerializer(api_details, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         api_details.delete()








# ---------------------request and response-------------------
# @api_view(['GET', 'POST'])
# def api_list(request):
   
#     if request.method == 'GET':
#         api_data = Contact.objects.all()
#         serializer = ContactSerializer(api_data, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
      
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_detail(request, pk):
   
#     try:
#         data_details = Contact.objects.get(pk=pk)
#     except Contact.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ContactSerializer(data_details)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ContactSerializer(data_details, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         data_details.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# ----------------------Class base view------------------------------

# class BlogList(APIView):
    
#     def get(self, request, format=None):
#         data_list = Contact.objects.all()
#         serializer = ContactSerializer(data_list, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
# class ApiDetail(APIView):
  
#     def get_object(self, pk):
#         try:
#             return Contact.objects.get(pk=pk)
#         except Contact.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         data_list = self.get_object(pk)
#         serializer = ContactSerializer(data_list)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         data_list = self.get_object(pk)
#         serializer = ContactSerializer(data_list, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         data_list = self.get_object(pk)
#         data_list.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
      
      
      
      
#------------------ganeric and mixins---------------------#

class ContactList(generics.ListCreateAPIView,mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset =Contact.objects.all()
    serializer_class = ContactSerializer
    
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request) 
      
      
      
class ContactDetail(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class =ContactSerializer
    
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





#-----------------Relationships & Hyperlinked APIs-------------

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('contact-list', request=request, format=format),
        
    })