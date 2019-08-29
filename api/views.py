#import datetime
#import json
#from django.views.decorators.csrf import csrf_exempt

#from django.shortcuts import render
#from api.models import Compra, Producto_compra, Producto
# Create your views here.
'''
@csrf_exempt
def checkout_cart(request):
    request_data = json.loads(request.body)
    print(request.body)
    cart_data  = request_data.get('items')
    compra = Compra.objects.create(fecha_compra=datetime.datetime.now())
    valor_compra = 0
    compra.save()
    for item in cart_data:
         producto=Producto.objects.get(id=item.get('id_producto'))
         no_productos = int(item.get('no_productos'))
         if producto and no_productos > 0 and producto.cantidad <= int(no_productos):
             producto_compra = Producto_compra.objects.create(compra=compra, producto=producto, no_productos=no_productos, precio_compra=producto.precio)
             valor_compra += producto.precio * no_productos
             producto_compra.save()
    compra.valor_compra = valor_compra
    compra.save()
    return json(compra)
'''
