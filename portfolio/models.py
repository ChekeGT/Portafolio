from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250 ,verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='Projects')
    url = models.URLField(null=True,blank=True,verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha De Creacion:')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha De Edicion')
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']
    def __str__(self):
        return self.title