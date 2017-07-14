# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Empresa, Menu, Carousel, Conteudo, Contato

admin.site.register(Empresa)
admin.site.register(Menu)
admin.site.register(Carousel)
admin.site.register(Conteudo)
admin.site.register(Contato)
