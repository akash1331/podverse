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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters


class allpodcastAPIView(APIView):
    def get(self,request):
        object = podcastDetails.objects.all()
        serializer = PodcastSerializer(object,many=True)
        return Response(serializer.data)
    
    def is_member(self,user):
        return user.groups.filter(name='Creator').exists()

    def post(self,request):
        # permission_classes = [IsAuthenticatedOrReadOnly]
        serializer = PodcastSerializer(data = request.data)
        if serializer.is_valid():
                if self.is_member(request.user):
                    
                    serializer.save()
                    return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
class eachPodcastDetail(APIView):
    def get_object(self,id):
        try:
            return podcastDetails.objects.get(id = id)
        except podcastDetails.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        articles = self.get_object(id)
        serializer = PodcastSerializer(articles)
        return Response(serializer.data)
    
    def is_member(self,user):
        return user.groups.filter(name='Creator').exists()

    def put(self,request,id):
        article  = self.get_object(id)
        serializer = PodcastSerializer(article,data = request.data)
        if serializer.is_valid():
            if self.is_member(request.user):
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    # def delete(self,request,id):
    #     article = self.get_object(id)
    #     serializer = PodcastSerializer(article,data = request.data)
    #     if serializer.is_valid():
    #         if self.is_member(request.user):
    #             article.delete()
    #             return Response(status = status.HTTP_204_NO_CONTENT)
    #     return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

# class PodcastSearchView(APIView):
#     def get(self, request, query):
#         podcast = podcastDetails.objects.filter(title__icontains=query)
#         results = []
#         for data in podcast:
#             results.append({
#                 'id': data.id,
#                 'title': data.podname,
#                 'desc': data.poddesc,
#                 'creator': data.podcreator,
#                 'date': data.dateuploaded
#             })
#         return Response({'results': results})

class PodcastSearchView(generics.ListCreateAPIView):
    search_fields = ['podname',]
    filter_backends = (filters.SearchFilter,)
    queryset = podcastDetails.objects.all()
    serializer_class = PodcastSerializer