# -*- coding: utf-8 -*-
from django.db import models

from django.conf import settings
from django_extensions.db.fields import UUIDField

import datetime, os

def profissional_curriculo_path(instance, filename):
    return os.path.join(
        'profissional/', instance.uuid, 'curriculo/', filename
      )

def profissional_foto_path(instance, filename):
    return os.path.join(
        'profissional/', instance.uuid, 'foto/', filename
      )


class Profissional(models.Model):
    
    def __unicode__(self):
        return "Nome: %s" % self.nome
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuário do Sistema", blank=True, null=True)
    uuid = UUIDField()
    nome = models.CharField(blank=False, max_length=500)
    email = models.EmailField()
    curriculo_texto = models.TextField(blank=True)
    curriculo_arquivo = models.FileField(upload_to=profissional_curriculo_path)
    foto = models.ImageField(upload_to=profissional_foto_path)
    # metadata
    criado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now_add=True, verbose_name="Criado")
    atualizado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now=True, verbose_name="Atualizado")        
    
