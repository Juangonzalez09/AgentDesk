
from django.contrib import admin
from django.urls import path
from AgentDesk.views import IndexView,HomeView,TicketsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView),
    path('Home/',HomeView),
    path('Home/Tickets',TicketsView)
    
]
