from rest_framework import serializers
from .models import ApiModel


class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiModel
        fields = ('title', 'description')
