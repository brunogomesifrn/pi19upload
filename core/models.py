from django.db import models

class Tipo(models.Model):
	nome = models.CharField('Nome', max_length=100)
	def __str__(self):
		return self.nome

class Doc(models.Model):
	nome = models.CharField('Nome', max_length=100)
	data = models.DateTimeField('Data')
	arquivo = models.FileField('Arquivo', upload_to='upload')
	local = models.CharField('Local Físico', max_length=100)
	remetente = models.CharField('Remetente', max_length=100)
	tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
