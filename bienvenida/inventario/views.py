from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Producto
from .forms import ProductoForm

# READ (List)
def producto_list(request):
    productos = Producto.objects.filter(activo=True).order_by('-fecha_creacion')
    return render(request, 'inventario/producto_list.html', {
        'object_list': productos
    })

# READ (Detail)
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'inventario/producto_detail.html', {
        'object': producto
    })

# CREATE
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" creado exitosamente.')
            return redirect('producto_detail', pk=producto.pk)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ProductoForm()
    
    return render(request, 'inventario/producto_form.html', {
        'form': form
    })

# UPDATE
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado exitosamente.')
            return redirect('producto_detail', pk=producto.pk)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'inventario/producto_form.html', {
        'form': form
    })

# DELETE
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        nombre_producto = producto.nombre
        
        # AJAX request handling
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            producto.activo = False  # Soft delete
            producto.save()
            return JsonResponse({
                'success': True,
                'message': f'Producto "{nombre_producto}" eliminado exitosamente.'
            })
        else:
            # Regular form submission
            producto.activo = False  # Soft delete
            producto.save()
            messages.success(request, f'Producto "{nombre_producto}" eliminado exitosamente.')
            return redirect('producto_list')
    
    return render(request, 'inventario/producto_confirm_delete.html', {
        'object': producto
    })