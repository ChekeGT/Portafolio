from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    relevant_image = models.ImageField(upload_to='Blog', verbose_name='Imagen de portada')
    introduction_text = models.TextField(verbose_name='Texto de introduccion',)
    content = RichTextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    reading_time = models.IntegerField(verbose_name='Tiempo de lectura(minutos)')
    category = models.CharField(max_length=50, verbose_name='Categoria')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
