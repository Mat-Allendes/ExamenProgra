from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import *


# Create your views here.
def root(request):
    return redirect('/index')

def index(request):
    return render (request,'core/index.html')

def tabacos(request):
    return render(request,'core/tabacos.html')    

def cigarros(request):
    return render(request,'core/cigarros.html')

def accesorios(request):
    return render(request,'core/accesorios.html')    

def nosotros(request):
    return render(request,'core/nosotros.html')

def suscripcion(request):
    return render(request,'core/suscripcion.html') 

def registro(request):
    if request.method=='POST':
        print('probando')
        #usernew=User.objects.create_user(username=request.POST['email'],email=request.POST['email'],password=request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['last_name'])
        #pepote=registro.objects.create(rut='20986847-1',fecha='1998-08-03',num=987654321,direccion='avenida asbdbasidco',id_Reg_id=usernew.id)
        #print(usernew)
    return render(request, 'core/registro.html')
