from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'subject', 'details']
