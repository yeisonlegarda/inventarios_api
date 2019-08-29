from rest_framework import generics
from rest_framework import viewsets

from .models import *
from .serializers import *



class ResponsableViewSet(generics.ListCreateAPIView):
    queryset = Responsable.objects.all()
    serializer_class = ResponsableListSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetalle(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_producto.objects.all()
    serializer_class = TipoProductoSerializer
