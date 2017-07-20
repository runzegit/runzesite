# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Empresa, Menu, Carousel, Conteudo, Contato
from .forms import ContatoForm
from django.http import HttpResponse
from django.core.mail import send_mail
import time
# Create your views here.

def home(request):
	empresa = Empresa.objects.get(pk=1)
	menus = Menu.objects.all()
	carousel = Carousel.objects.all()
	form = ContatoForm()
	for menu in menus:
		conteudos = Conteudo.objects.filter(menu=menu)
	menu.conteudos = conteudos
	return render(request, 'runze/home.html', {'empresa':empresa, 'menus': menus, 'carousel': carousel, 'form': form})

def contato(request):
	if request.method == "POST":
		form = ContatoForm(request.POST)
		if form.is_valid():
			contato = form.save(commit=False)
			contato.save()
			empresa = Empresa.objects.get(pk=1)
			texto = 'Nome: '+contato.nome+'\n\r'+'Telefone: '+contato.telefone+'\n\r'+'E-mail: '+contato.email+'\n\r'+'Data: '+str(contato.data)+'\n\r\n\r'+'Assunto: '+contato.assunto+'\n\r\n\r'+'Mensagem: '+contato.texto
			time.sleep(5)
			#send_mail('Site: '+contato.nome+' - '+contato.assunto, texto, 'runzegit@gmail.com', ['runzegit@gmail.com'], fail_silently=False, )
			return render(request, 'runze/form-contato.html', {'form': ContatoForm(), 'resposta': 'Mensagem enviada com sucesso! Obrigado!'})
		return render(request, 'runze/form-contato.html', {'form': ContatoForm(), 'resposta': 'Ocorrou algum problema ao enviar mensagem, tente novamente mais tarde. Obrigado'})