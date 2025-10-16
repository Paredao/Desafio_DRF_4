from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usuario, Chamado
from .serializers import UsuarioSerializer, ChamadoSerializer

class UsuarioChamadosListView(generics.ListAPIView):
    serializer_class = ChamadoSerializer
    
    def get_queryset(self):
        usuario_id = self.kwargs['id']
        return Chamado.objects.filter(usuario_id=usuario_id)

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ChamadoListCreateView(generics.ListCreateAPIView):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer

class ChamadoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer
