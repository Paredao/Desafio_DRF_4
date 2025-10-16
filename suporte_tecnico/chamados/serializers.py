from rest_framework import serializers
from .models import Usuario, Chamado

class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        fields = ['id', 'titulo', 'descricao', 'data_criacao']

class UsuarioSerializer(serializers.ModelSerializer):
    chamados = ChamadoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'chamados']