from django.forms import ModelForm
from .models import Doc, Tipo
from django.contrib.auth.forms import UserCreationForm

class DocForm(ModelForm):
	class Meta():
		model = Doc
		fields = ['nome', 'data', 'arquivo', 'local', 'remetente', 'grupo', 'tipo']

	def __init__(self, usuario, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['grupo'].queryset = usuario.groups.all()

class TipoForm(ModelForm):
	class Meta():
		model = Tipo
		fields = ['nome']

class UsuarioForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		fields = ['username', 'is_superuser', 'groups', 'password1', 'password2']

