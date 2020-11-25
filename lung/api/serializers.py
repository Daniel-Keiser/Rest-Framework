from rest_framework.serializers import ModelSerializer
from lung.models import Lung



class LungSerializer(ModelSerializer):
    class Meta:
        model = Lung
        fields = ('id','nome', 'descricao', 'horario_funcionamento', 'idade_minima', 'foto')