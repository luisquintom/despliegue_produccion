from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Agencia, Mision
from .serializers import AgenciaSerializer, MisionSerializer

# --- 4 Vistas Genéricas para AGENCIA (Requisito) ---
class AgenciaList(generics.ListAPIView):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer

class AgenciaCreate(generics.CreateAPIView):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer

class AgenciaDetail(generics.RetrieveAPIView):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer

class AgenciaDelete(generics.DestroyAPIView):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer
    # SEGURIDAD (Requisito 1.2): Solo borra quien tenga permiso
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

# --- ViewSet para MISION (Requisito) ---
class MisionViewSet(viewsets.ModelViewSet):
    queryset = Mision.objects.all()
    serializer_class = MisionSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

# --- API View Propia: Buscador (Requisito) ---
@api_view(['GET'])
def buscar_misiones_por_agencia(request, nombre_agencia):
    # Enlace de modelos: Mision -> Agencia -> nombre
    misiones = Mision.objects.filter(agencia__nombre__icontains=nombre_agencia)

    # Manejo de Errores (Feedback usuario)
    if not misiones.exists():
        return Response({"mensaje": "No se encontraron misiones para esa agencia"}, status=404)

    serializer = MisionSerializer(misiones, many=True)
    return Response(serializer.data)