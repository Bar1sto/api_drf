from rest_framework import viewsets
from .serializers import ApiSerializer
from .models import ApiModel


class ApiViesSet(viewsets.ModelViewSet):
    queryset = ApiModel.objects.all()
    serializer_class = ApiSerializer