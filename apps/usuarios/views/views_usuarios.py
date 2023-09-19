from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from forms import RegistroUsuarioForm

#-- Registrar Usuario ---------------------------------------------------------
def registrar_usuario(request):
	if request.method == 'POST':
		form = RegistroUsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			usuario = authenticate(
				request, 
				username=form.cleaned_data['username'], 
				password=form.cleaned_data['password1']
			)
			login(request, usuario)
			return redirect('inicio')
	else:
		form = RegistroUsuarioForm()
	
	context = {'form':form}
	return render(request, 'registrar_usuario.html', context)


#-- Iniciar Sesión ------------------------------------------------------------
def iniciar_sesion(request):
	if request.method == "GET":
		return render(request, 'iniciar_sesion.html', {
			'form': AuthenticationForm
		})
	else:
		user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
		if user is None:
			return render(request, 'iniciar_sesion.html', {
				'form': AuthenticationForm,
				'error': 'Usuario/Clave incorrecto o no existe el usuario.'
			})
		else:
			login(request, user)
			return redirect('inicio')


#-- Cerrar Sesión -------------------------------------------------------------
@login_required
def cerrar_sesion(request):
	logout(request)
	return redirect('iniciar_sesion')
