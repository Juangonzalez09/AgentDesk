
from django.contrib import admin
from django.urls import path
from AgentDesk.views import IndexView,HomeView,TicketsView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView),
    path('Home/',HomeView),
    path('Home/Ticket/<int:ticket_id>/',TicketsView,name="detailTicket"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
]
