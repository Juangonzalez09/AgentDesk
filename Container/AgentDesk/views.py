from django.shortcuts import render

#Funcion index principal

def IndexView(request):
    return render(request,"index.html")