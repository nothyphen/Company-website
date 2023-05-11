from rest_framework import serializers
from django.utils import timezone
from blog import models
from django.contrib.auth.models import User

class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"