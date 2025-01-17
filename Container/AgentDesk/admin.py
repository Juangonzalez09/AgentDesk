from django.contrib import admin
from .models import teams,profile,tickets

class teamsAdmin(admin.ModelAdmin):
    fields = ["team"]
    list_display = ["team"]
    
admin.site.register(teams,teamsAdmin)

class profileAdmin(admin.ModelAdmin):
    fields = ["name","role","id_team","user"]
    list_display = ["name","role","id_team","user"]
    
class ticketsAdmin(admin.ModelAdmin):
    fields = ["title","description","client","email","contact","type_error","created_by","assigned_to","state"]
    list_display = ["title","description","client","email","contact","type_error","created_by","assigned_to","state"]

admin.site.register(profile,profileAdmin)
admin.site.register(tickets,ticketsAdmin)

