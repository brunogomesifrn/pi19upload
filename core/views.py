from django.shortcuts import render, redirect
from .models import Doc, Tipo
from .forms import DocForm, TipoForm, UsuarioForm

#OUTRA COISA
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required	
def listar(request):
	doc = Doc.objects.filter(grupo__in=request.user.groups.all())
	search = request.GET.get('search')
	if search:	
		doc = doc.filter(nome__icontains=search) or doc.filter(local__icontains=search) or doc.filter(remetente__icontains=search) or doc.filter(data__icontains=search)
	contexto = {'doc_listar': doc}
	return render(request, 'doc_lista.html', contexto)

@login_required
def cadastro(request):
	form = 	DocForm(request.user, data=request.POST or None, files=request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('doc')

	contexto = {
		'form': form
	}
	return render(request, 'doc_cadastro.html', contexto)

@login_required
def atualizar(request, id):
	doc = Doc.objects.get(pk=id)
	form = DocForm(request.user, data=request.POST or None, files=request.FILES or None, instance=doc)
	if form.is_valid():
		form.save()
		return redirect('doc')
	contexto = {
		'form': form
	}
	return render(request, 'doc_cadastro.html', contexto)

@login_required
def deletar(request, id):
	doc = Doc.objects.get(pk=id)
	doc.delete()
	return redirect('doc')

#Tipo
@login_required
def tipo_listar(request):
	tipo = Tipo.objects.all()
	contexto = {
		'tipo_listar': tipo
	}
	return render(request, 'tipo.html', contexto)

@login_required
def tipo_cadastrar(request):
	form = 	TipoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('tipo')

	contexto = {
		'form': form
	}
	return render(request, 'tipo_cadastro.html', contexto)

@login_required
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

@login_required
def tipo_deletar(request, id):
	tipo = Tipo.objects.get(pk=id)
	tipo.delete()
	return redirect('tipo')

#Area
@login_required
def area(request):
	categoria = Tipo.objects.all()
	contexto = {
		'categorias': categoria
	}
	return render(request, 'area.html', contexto)

@login_required
def filtrar(request, categoria_id):
	doc = Doc.objects.filter(tipo=categoria_id, grupo__in=request.user.groups.all())
	contexto = {'doc_listar': doc}
	return render(request, 'doc_lista.html', contexto)


#Login e cadastro
@login_required
def index(request):
	return render(request, "index.html")
@login_required
def perfil(request):
	return render(request, "perfil.html")

@login_required
def registro(request):
	form = UsuarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form.save_m2m()
		return redirect('login')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)

@login_required
def dados(request, id):
	user = User.objects.get(pk=id)
	form = UsuarioForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	contexto = {
		'form': form
	}
	return render(request, 'registro.html', contexto)



















