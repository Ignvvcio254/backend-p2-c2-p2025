from django.contrib import admin
from .models import Producto

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'activo', 'fecha_creacion']
    list_filter = ['activo', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio', 'stock', 'activo']
    actions = ['delete_selected']
    
    def delete_selected(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f'{count} productos eliminados exitosamente.')
    delete_selected.short_description = "Eliminar productos seleccionados"