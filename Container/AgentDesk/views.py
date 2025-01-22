from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , JsonResponse
from .forms import LoginForm,commentForm
from .models import profile,tickets,comment
#Funcion index principal

def IndexView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/Home/')
                else:
                    return HttpResponse('El usuario no esta activo')
            else:
                return HttpResponse('La informacion del usuario no es correcta')
    else:
         form = LoginForm()     
         return render(request,'index.html',{'form':form})  

@login_required(login_url='/')
def HomeView(request):
    # Obtener el usuario que ha iniciado sesión
    user = request.user
    try:
        profileq = profile.objects.get(user=user)
        
    except profileq.DoesNotExist:

        profileq = None
    
    #validar error de usuario NONE
    id_teamq = profileq.id_team
    
    Tickets_q = tickets.objects.filter(type_error=id_teamq)
    
    return render(request,"pages/home.html",{'Tickets_q':Tickets_q})
    

@login_required(login_url='/')

def TicketsView(request,ticket_id):
    ticket = get_object_or_404(tickets,id=ticket_id)
    commentq = comment.objects.filter(ticket=ticket)  
    users = profile.objects.filter(id_team=ticket.type_error)
    
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)  # No lo guardes aún
            comentario.ticket = ticket  # Asigna el ticket al comentario
            comentario.save()  # Ahora sí, guárdalo
            return redirect(request.path)  # Recarga la página para ver el comentario agregado
    else :
            
            form = commentForm()
            return render(request, 'pages/detailTicket.html',{'ticket':ticket,
                                                        'commentq' : commentq,
                                                        'form':form,
                                                        'users':users,
                                                        'prioritis' : tickets.PRIORITY_CHOICES
                                                        
                                                  })
            
    

    

