from django.contrib import admin
from .models import teams,profile,tickets

class teamsAdmin(admin.ModelAdmin):
    fields = ["team"]
    list_display = ["team"]
    
admin.site.register(teams,teamsAdmin)

class profileAdmin(admin.ModelAdmin):
    fields = ["name","role","id_team","user"]
    list_display = ["name","role","id_team","user"]
    
admin.site.register(profile,profileAdmin)
admin.site.register(tickets)
