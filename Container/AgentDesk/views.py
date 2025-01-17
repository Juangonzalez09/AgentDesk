from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm
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
                    return HttpResponse('Usuario Aunteticado')
                else:
                    return HttpResponse('El usuario no esta activo')
            else:
                return HttpResponse('La informacion del usuario no es correcta')
    else:
         form = LoginForm()     
         return render(request,'index.html',{'form':form})  

def HomeView(request):
    return render(request,"base.html")


def TicketsView(request):
    return render(request,"pages/home.html")