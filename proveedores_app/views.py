from django.shortcuts import render

# Create your views here.
def vista_proveedores(request):
    proveedor_list = [
        {"nombre_proveedor": "VIDCLA"},
        {"nombre_proveedor": "SOBOLMA"},
        {"nombre_proveedor": "MZ40"}
    ]

    context = {
        "proveedores": proveedor_list
    }

    return render(request, "proveedores_app/proveedor_list.html",context)