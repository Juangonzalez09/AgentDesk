from django.contrib import admin
from .models import teams,users,tickets

admin.site.register(teams)
admin.site.register(users)
admin.site.register(tickets)