# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

import datetime, os 

from django_extensions.db.fields import UUIDField

# Create your models here.

def empregador_logo_path(instance, filename):
    return os.path.join(
        'empregador/', instance.uuid, 'logo/', filename
      )

class Empregador(models.Model):
    
    def __unicode__(self):
        return self.nome
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuário do Sistema", blank=True, null=True)
    uuid = UUIDField()
    logo = models.ImageField(upload_to=empregador_logo_path)
    nome = models.CharField(blank=True, max_length=100)
    telefone = models.CharField(blank=True, max_length=100)
    descricao = models.CharField(blank=True, max_length=100)
    # metadata
    criado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now_add=True, verbose_name="Criado")
    atualizado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now=True, verbose_name="Atualizado")        