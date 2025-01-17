from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
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
    return render(request,"base.html")

@login_required(login_url='/')
def TicketsView(request):
    return render(request,"pages/home.html")
