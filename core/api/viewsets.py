from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.views import Response
from rest_framework.request import Request
from core.models import Brain
from .serializers import BrainSerializer

 
class BrainViewSet(ModelViewSet):
    serializer_class= BrainSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    search_fields = ('id', 'nome','descricao', 'enderecos__descricao')
    lookup_field = 'nome'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = Brain.objects.all()

        if id:
            queryset = Brain.objects.filter(pk=id)

        if nome:
            queryset.filter(nome__iexact=nome)

        if descricao:
            queryset.filter(descricao__iexact=descricao)
        

        return queryset
    
    def list(self, request, *args, **kwargs):
        return super(BrainViewSet, self). list (request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(BrainViewSet, self). create (request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(BrainViewSet, self). delete (request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(BrainViewSet, self). destroy (request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(BrainViewSet, self). update (request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(BrainViewSet, self). partial_update (request, *args, **kwargs)
