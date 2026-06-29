# Importamos funciones útiles de Django:
# - render: renderiza archivos HTML
# - redirect: redirecciona a otra URL
# - get_object_or_404: busca un objeto; si no existe, lanza error 404
from django.shortcuts import render, redirect, get_object_or_404

# Decorador para permitir acceso solo a usuarios autenticados.
from django.contrib.auth.decorators import login_required

# Importamos los modelos principales del módulo checkout.
from .models import Checkout, Pago

# Importamos el modelo del carrito para acceder a los productos agregados.
from carrito.models import Carrito

# Importamos modelos de pedidos.
# Pedido = orden general de compra
# Detalle_pedido = productos específicos dentro del pedido
from pedidos.models import Pedido, Detalle_pedido

# Importamos los formularios que llenará el usuario.
from .forms import CheckoutForm, PagoForm


# JsonResponse permite devolver datos en formato JSON.
# Es útil para AJAX (JavaScript asíncrono).
from django.http import JsonResponse

# Modelos geográficos para filtros dinámicos.
from .models import Municipio, Barrio



# =========================
# VISTA PRINCIPAL CHECKOUT
# =========================

# Esta vista controla todo el proceso de checkout:
# 1. Verifica usuario autenticado
# 2. Obtiene carrito
# 3. Muestra formularios
# 4. Procesa pago
# 5. Genera pedido

@login_required
def checkout_view(request):

    # Obtiene el cliente asociado al usuario logueado.
    cliente = request.user.cliente

    # Busca el carrito del cliente.
    # Si no existe, Django devuelve error 404 automáticamente.
    carrito = get_object_or_404(Carrito, cliente=cliente)

    # Obtiene todos los productos agregados al carrito.
    items_carrito = carrito.item_carrito_set.all()

    # Si el carrito está vacío, no tiene sentido hacer checkout.
    # Por eso se redirecciona al carrito.
    if not items_carrito.exists():
        return redirect("ver_carrito")



    # Si el usuario envió el formulario (dio clic en pagar)
    if request.method == "POST":

        # Cargamos los datos enviados al formulario.
        checkout_form = CheckoutForm(request.POST)
        pago_form = PagoForm(request.POST)

        # Validamos ambos formularios.
        if checkout_form.is_valid() and pago_form.is_valid():

            # Guardamos checkout sin enviarlo todavía a la BD.
            # commit=False permite modificar campos antes del save final.
            checkout = checkout_form.save(commit=False)

            # Asignamos el cliente automáticamente.
            checkout.cliente = cliente

            # Ahora sí guardamos en la base de datos.
            checkout.save()



            # =========================
            # CREACIÓN DEL PEDIDO
            # =========================

            # Se crea un pedido con estado pendiente.
            pedido = Pedido.objects.create(
                cliente=cliente,
                checkout=checkout,
                estado="Pagado"
            )

            # =========================
            # CREACIÓN DE DETALLES DEL PEDIDO
            # =========================

            # Recorremos cada item del carrito.
            for item in items_carrito:

                # Por cada producto se crea una fila en detalle_pedido.
                # Esto guarda qué productos compró y cuántos.
                Detalle_pedido.objects.create(
                    pedido=pedido,
                    producto=item.producto,
                    cantidad=item.cantidad
                )

            # =========================
            # REGISTRO DEL PAGO
            # =========================

            # Guardamos pago temporalmente.
            pago = pago_form.save(commit=False)

            # Asociamos el pago al checkout.
            pago.checkout = checkout

            # En este sistema se aprueba automáticamente.
            # (En sistemas reales esto lo decide una pasarela de pago)
            pago.estado = "Aprobado"

            # Generamos referencia única.
            # Ejemplo: REF-12-5
            # checkout 12, cliente 5
            pago.referencia = f"REF-{checkout.id}-{cliente.id}"

            # Guardamos pago.
            pago.save()

            # =========================
            # LIMPIAR CARRITO
            # =========================

            # Como ya compró, eliminamos items del carrito.
            items_carrito.delete()



            # Redireccionamos al detalle del pedido.
            return redirect("detalle_pedido", pedido.id)



    # Si la petición fue GET (solo abrir página)
    else:

        # Se muestran formularios vacíos.
        checkout_form = CheckoutForm()
        pago_form = PagoForm()
    


    # =========================
    # CALCULAR TOTAL
    # =========================

    # Suma subtotal de cada producto del carrito.
    total = sum(item.subtotal for item in items_carrito)



    # =========================
    # RENDER DEL TEMPLATE
    # =========================

    # Enviamos toda la información al HTML.
    return render(request, "checkout/checkout.html", {
        "checkout_form": checkout_form,
        "pago_form": pago_form,
        "items_carrito": items_carrito,
        "carrito": carrito,
        "total": total
    })



# =========================
# VISTAS AJAX
# =========================

# Estas vistas permiten cargar municipios y barrios dinámicamente
# sin recargar la página completa.



# Vista para obtener municipios según el departamento seleccionado.
def cargar_municipios(request):

    # Obtiene el id del departamento enviado por AJAX.
    departamento_id = request.GET.get('departamento')

    # Filtra municipios que pertenezcan a ese departamento.
    municipios = Municipio.objects.filter(
        departamento_id=departamento_id
    ).order_by('nombre')

    # Devuelve JSON:
    # [
    #   {"id":1, "nombre":"Pereira"},
    #   {"id":2, "nombre":"Dosquebradas"}
    # ]
    return JsonResponse(
        list(municipios.values('id', 'nombre')),
        safe=False
    )



# Vista para obtener barrios según municipio seleccionado.
def cargar_barrios(request):

    # Obtiene municipio desde AJAX.
    municipio_id = request.GET.get('municipio')

    # Filtra barrios correspondientes.
    barrios = Barrio.objects.filter(
        municipio_id=municipio_id
    ).order_by('nombre')

    # Devuelve lista JSON.
    return JsonResponse(
        list(barrios.values('id', 'nombre')),
        safe=False
    )