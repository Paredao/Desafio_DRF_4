from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/<int:id>/chamados/', views.UsuarioChamadosListView.as_view(), name='usuario-chamados'),
    path('usuarios/', views.UsuarioListCreateView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('chamados/', views.ChamadoListCreateView.as_view(), name='chamado-list'),
    path('chamados/<int:pk>/', views.ChamadoDetailView.as_view(), name='chamado-detail'),
]