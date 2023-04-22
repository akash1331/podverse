from httplib2 import Authentication
from rest_framework.generics import ListAPIView
from django_filters.rest_framework  import DjangoFilterBackend
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# import authentications
# from authentications.models import *
from .models import *
from rest_framework.parsers import JSONParser
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework import generics
from rest_framework import mixins