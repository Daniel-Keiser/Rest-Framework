from rest_framework.viewsets import ModelViewSet
from lung.models import Lung
from .serializers import LungSerializer


class LungViewSet(ModelViewSet):
    queryset = Lung.objects.all()
    serializer_class = LungSerializer