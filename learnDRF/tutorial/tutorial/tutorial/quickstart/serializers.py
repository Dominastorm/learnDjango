from django.contrib.auth.models import User, Group
from rest_framework import serializers

# This file stores our data representaions
# Primary key and other relationships can also be used bur Hyperlinking is a good RESTful practice

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']