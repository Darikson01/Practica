from enum import Flag
from django.db import models
from django.utils.html import format_html

class Equipment (models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre del equipo")
    flag = models.ImageField(upload_to='media/', null=True, verbose_name="Escudo del equipo")
    shield = models.ImageField(upload_to='media/', null=True, verbose_name="Escudo del equipo")
    
    def __str__(self) :
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        self.flag.storage.delete(self.flag.name)
        super().delete()

    def Escudo(self):
        return format_html('<img src={} width="100" />', self.flag.url)

    def Bandera(self):
        return format_html('<img src={} width="100" />', self.shield.url)
        
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'equipo'
        ordering = ['id']
        
class Position (models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de la posición")
    description = models.TextField(verbose_name="Descripción", null=True)
    
    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name = 'Posicion'
        verbose_name_plural = 'Posiciones'
        db_table = 'posicion'
        ordering = ['id']
        
class Player (models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre del jugador")
    surname = models.CharField(max_length=30, verbose_name="Apellido del jugador")
    photo = models.ImageField(upload_to='media/', null=True, verbose_name="Foto del jugador")
    birth = models.DateField(verbose_name="Fecha de nacimiendo")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Posicion del jugador")
    tshirt = models.IntegerField(verbose_name="Numero de camiseta")
    headline = models.BooleanField (verbose_name="¿El jugador es titular?")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Equipo del jugador")
    
    def __str__(self) :
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        self.photo.storage.delete(self.photo.name)
        super().delete()

    def Foto_del_jugador(self):
        return format_html('<img src={} width="100" />', self.photo.url)
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        db_table = 'jugador'
        ordering = ['id']
               
class Technical (models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre del tecnico")
    surname = models.CharField(max_length=30, verbose_name="Apellido del tecnico")
    birth = models.DateField(verbose_name="Fecha de nacimiendo")
    Nationality = models.CharField(max_length=40,verbose_name="Nacionalidad")
    
    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        db_table = 'tecnico'
        ordering = ['id']
