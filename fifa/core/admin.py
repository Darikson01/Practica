from django.contrib import admin
from .models import  Equipment, Player,Position,Technical

class ListEqui(admin.ModelAdmin):
    list_display = ["name", "Escudo", "Bandera"]

class ListPla (admin.ModelAdmin):
    list_display = ["name", "surname",  "Foto_del_jugador", "birth", "position", "tshirt", "headline", "equipment"] 

class ListPosi(admin.ModelAdmin):
    list_display = ["name", "description"]

class listTec(admin.ModelAdmin):
    list_display= ["name", "surname", "birth", "Nationality"]


admin.site.register(Equipment,ListEqui)
admin.site.register(Position,ListPosi)
admin.site.register(Player,ListPla)
admin.site.register(Technical,listTec)
