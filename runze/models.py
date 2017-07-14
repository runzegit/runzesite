from __future__ import unicode_literals
from django.db import models

class Empresa(models.Model):
	nome = models.CharField(max_length=200)
	telefone = models.CharField(max_length=20)
	email = models.CharField(max_length=200)
	logo = models.ImageField(upload_to='empresa/')
	endereco = models.CharField(max_length=400)

	def __str__(self):
		return self.nome

class Menu(models.Model):
	nome = models.CharField(max_length=200)
	titulo = models.CharField(max_length=200)
	descricao = models.CharField(max_length=400)
	tipo = models.IntegerField()
	imagem = models.ImageField(upload_to='menu/', blank=True)

	def __str__(self):
		return self.titulo

class Carousel(models.Model):
	imagem = models.ImageField(upload_to='carousel/')
	ordem = models.CharField(max_length=20)
	titulo = models.CharField(max_length=200)
	descricao = models.CharField(max_length=400)

	def __str__(self):
		return self.titulo

class Conteudo(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	ordem = models.IntegerField()
	titulo = models.CharField(max_length=200)
	subtitulo = models.CharField(max_length=200)
	texto = models.TextField()
	imagem = models.ImageField(upload_to='conteudo/')

	def __str__(self):
		return self.titulo+' - '+self.menu.titulo

class Contato(models.Model):
	nome = models.CharField('Nome', max_length=200)
	telefone = models.CharField('Telefone', max_length=20)
	email = models.CharField('E-mail', max_length=200)
	assunto = models.CharField('Assunto', max_length=200)
	texto = models.TextField('Mensagem')
	data = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.nome+' - '+self.assunto


