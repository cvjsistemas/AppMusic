from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def home(request):
    discos = Product.objects.all()
    return render(request,'gestionDiscos.html',{'discos':discos})

def registroDisco(request):
    product_nombre=request.POST['txtNombre']
    product_description=request.POST['txtDesc']
    product_price=request.POST['txtPrecio']

    disco=Product.objects.create(
        product_nombre=product_nombre,
        product_description=product_description,
        product_price=product_price
        )
    return redirect('/')

def edicionDisco(request,product_id):
    disco = Product.objects.get(product_id=product_id)
    return render(request,'edicionDisco.html',{'disco':disco})

def editarDisco(request):
    product_id=request.POST['txtID']
    product_nombre=request.POST['txtNombre']
    product_description=request.POST['txtDesc']
    product_price=request.POST['txtPrecio']

    disco = Product.objects.get(product_id=product_id)
    disco.product_nombre=product_nombre
    disco.product_description=product_description
    disco.product_price=product_price
    disco.save()

    return redirect('/')


def eliminarDisco(request,product_id):
    disco = Product.objects.get(product_id=product_id)
    disco.delete()

    return redirect('/')


def signup(request):

    if request.method =='GET':
        return render(request,'signup.html',{'from':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('inicio')
            except:
                return render(request,'signup.html',{'from':UserCreationForm,'error':'usuario ya existe'})
        
        return render(request,'signup.html',{'from':UserCreationForm,'error':'password no coincide'})
            
 

def signout(request):
    logout(request)
    return redirect('inicio')

def signin(request):
       if request.method =='GET':
           return render(request,'signin.html',{'from':AuthenticationForm})
       else:
           user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
           if user is None:
               return render(request,'sigin.html',{'from':AuthenticationForm,'error':'Datos incorrectos'})
           else:
               login(request,user)
               return redirect('inicio')





