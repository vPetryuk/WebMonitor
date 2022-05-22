from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import FailureSerializer, WebPageSerializer
from monitor.models import WebPage , Failure
from rest_framework import viewsets

class WebPageViewSet(viewsets.ModelViewSet):
   
    serializer_class = WebPageSerializer
    queryset = WebPage.objects.all()

class FailuresViewSet(viewsets.ModelViewSet):
    serializer_class = FailureSerializer
    queryset = Failure.objects.all()

