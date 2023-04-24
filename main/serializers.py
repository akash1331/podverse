import rest_framework
from rest_framework import serializers
from .models import *

class PodcastSerializer(serializers.ModelSerializer):
    class Meta():
        model = podcastDetails
        fields = '__all__'
    


# class admingrantSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Genre
#         fields = "__all__"

# class LanguageSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Language
#         fields = "__all__"
