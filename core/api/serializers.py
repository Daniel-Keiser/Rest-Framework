from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import Brain
from lung.api.serializers import LungSerializer 
from enderecos.api.serializers import EnderecoSerializer 

class BrainSerializer(ModelSerializer):
    lung = LungSerializer(many=True)
    enderecos = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = Brain
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'lung', 'enderecos', 'descricao_completa')

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)