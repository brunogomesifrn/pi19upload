from django.shortcuts import render, redirect
from .models import Doc
from .forms import DocForm

#OUTRA COISA
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def listar(request):
	doc = Doc.objects.all()
	contexto = {
		'doc_listar': doc
	}
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
		return redirect('festival')
	contexto = {
		'form': form
	}
	return render(request, 'doc_cadastro.html', contexto)

def deletar(request, id):
	doc = Doc.objects.get(pk=id)
	doc.delete()
	return redirect('doc')





#OUTRA COISA

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


















