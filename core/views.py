from django.shortcuts import render, redirect
from .models import Doc, Tipo
from .forms import DocForm, TipoForm

#OUTRA COISA
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

	
def listar(request):
	doc = Doc.objects.all()
	search = request.GET.get('search')
	if search:	
		doc = doc.filter(nome__icontains=search) or doc.filter(local__icontains=search) or doc.filter(remetente__icontains=search) or doc.filter(data__icontains=search)
	contexto = {'doc_listar': doc}
	return render(request, 'doc_lista.html', contexto)

def cadastro(request):
	form = 	DocForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('doc')

	contexto = {
		'form': form
	}
	return render(request, 'doc_cadastro.html', contexto)

def atualizar(request, id):
	doc = Doc.objects.get(pk=id)
	form = DocForm(request.POST or None, request.FILES or None, instance=doc)
	if form.is_valid():
		form.save()
		return redirect('doc')
	contexto = {
		'form': form
	}
	return render(request, 'doc_cadastro.html', contexto)

def deletar(request, id):
	doc = Doc.objects.get(pk=id)
	doc.delete()
	return redirect('doc')

#Tipo
def tipo_listar(request):
	tipo = Tipo.objects.all()
	contexto = {
		'tipo_listar': tipo
	}
	return render(request, 'tipo.html', contexto)

def tipo_cadastrar(request):
	form = 	TipoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('tipo')

	contexto = {
		'form': form
	}
	return render(request, 'tipo_cadastro.html', contexto)

def tipo_atualizar(request, id):
	tipo = Tipo.objects.get(pk=id)
	form = TipoForm(request.POST or None, instance=tipo)
	if form.is_valid():
		form.save()
		return redirect('tipo')
	contexto = {
		'form': form
	}
	return render(request, 'tipo_cadastro.html', contexto)

def tipo_deletar(request, id):
	tipo = Tipo.objects.get(pk=id)
	tipo.delete()
	return redirect('tipo')

#Area
def area(request):
	return render(request, "area.html")

#Login e cadastro

def index(request):
	return render(request, "index.html")
@login_required
def perfil(request):
	return render(request, "perfil.html")


def registro(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)

@login_required
def dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)


















