from django.urls import path,include
from api.apiviews import *
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
#from api.views import checkout_cart

schema_view = get_swagger_view(title="Restful api para inventarios")

router = DefaultRouter()

router.register('v1/productos',ProductoViewSet, base_name='productos')
router.register('v1/personas',PersonaViewSet, base_name='personas')
router.register('v1/areas',AreaViewSet, base_name='areas')
router.register('v1/estados',EstadoViewSet, base_name='estados')
router.register('v1/tiposproducto',TipoProductoViewSet, base_name='tipos producto')


urlpatterns = [
    path('swagger-doc/',schema_view),
    path('v1/responsables',ResponsableViewSet,name='responsables')
    #path('v1/producto_compra/',Producto_compraViewSet,name='producto compra'),
    #path('v1/producto_compra/',checkout_cart,name='producto compra')
]
urlpatterns += router.urls
