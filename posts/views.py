from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class IndexPageView(generics.GenericAPIView):
    
    def get(self, request):
        context = {}
        context['text'] = 'hello world'
        return Response(context, status=status.HTTP_200_OK)