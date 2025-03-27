from django.db import models

# Definir el modelo Categoria
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria


# Definir el modelo Proveedor
class Proveedor(models.Model):
    categoria_id = models.ForeignKey(Categoria, on_delete=models.RESTRICT)  # Relación de clave foránea
    nombre_proveedor = models.CharField(max_length=100)
    grupo = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre_proveedor