from django.forms import ModelForm
from .models import Doc, Tipo

class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome', 'data', 'arquivo', 'local', 'remetente', 'tipo']

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']