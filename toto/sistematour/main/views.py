from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}
from django.contrib.auth.forms import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from main.models import *

import pprint
# Create your views here.
# Create your views here.





def v_logout(request):
    try:
        _user = request.user
        logout(request)
    except Exception, e:
        print e
    return HttpResponseRedirect(reverse_lazy("principal"))

def login(request):
    mensaje=False
    if request.method == 'POST':
        formularioLogin = AuthenticationForm(request.POST)
        if formularioLogin.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    auth_login(request,acceso)
                    return HttpResponseRedirect(reverse_lazy("principal"))
                else:
                    mensaje="Su Usuario No esta Activo"
            else:
                mensaje="Su username o password estan incorrentos, vuelvelo a intentar"
        else:
            mensaje="Su username o password estan incorrentos, vuelvelo a intentar"

    formularioLogin = AuthenticationForm(request.POST)
    if mensaje:
        return render_to_response('login.html',{'mensaje':mensaje,'formulario':formularioLogin},context_instance=RequestContext(request)) 
    else:
        return render_to_response('login.html',{'formulario':formularioLogin},context_instance=RequestContext(request))  

@login_required(login_url='/login')
def principal(request):
 
    usuario=User.objects.get(pk=request.user.pk)  

    template = "index.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login')
def destinos(request):
    usuario=User.objects.get(pk=request.user.pk)
    destinos=Destino.objects.filter(es_activo=True)
    return render_to_response('destino.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/login')
def buses(request):
    usuario=User.objects.get(pk=request.user.pk)
    buses=Vehiculo.objects.filter(es_activo=True)
    return render_to_response('buses.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/login')
def generarorden(request):
    destinos=Destino.objects.filter(es_activo=True)
    buses=Vehiculo.objects.filter(es_activo=True)

    return render_to_response('generarorden.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/login')
def misdatos(request):


    usuario=User.objects.get(pk=request.user.pk)
    perfil=Usuario.objects.get(usuario=usuario)
    return render_to_response('misdatos.html',locals(),context_instance=RequestContext(request))

@login_required(login_url='/login')
def registardatos(request):

    cedula=request.POST.get("cedula")
    celular=request.POST.get("celular")
    pprint.pprint(cedula) 
    pprint.pprint(celular) 
    return HttpResponseRedirect(reverse_lazy("misdatos"))   
   