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

class RamoEmpregador(models.Model):
    
    def __unicode__(self):
        return self.nome
    
    nome = models.CharField(blank=True, max_length=100)

class Empregador(models.Model):
    
    def __unicode__(self):
        return self.nome
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuário do Sistema", blank=True, null=True)
    uuid = UUIDField()
    logo = models.ImageField(upload_to=empregador_logo_path, blank=True)
    nome = models.CharField(blank=False, max_length=100)
    telefone = models.CharField(blank=False, max_length=100)
    historico = models.CharField(blank=True, max_length=100)
    #DADOS RESPONSAVEL CADASTRO
    nome_responsavel = models.CharField(blank=True, max_length=100)
    sobre_nome_responsavel = models.CharField(blank=True, max_length=100)
    email_responsavel = models.EmailField()
    # INFORMACOES CADASTRAIS EMPRESA
    nome_fantasia = models.CharField(blank=True, max_length=100)
    razao_social = models.CharField(blank=False, max_length=100)
    ramo = models.ForeignKey("RamoEmpregador")
    cnpj = models.CharField(blank=True, max_length=100)
    # endereco empregador
    endereco = models.CharField(blank=True, max_length=500)
    numero = models.CharField(blank=True, max_length=100)
    complemento = models.CharField(blank=True, max_length=100)
    bairro = models.CharField(blank=True, max_length=100)
    cep = models.CharField(blank=True, max_length=100)
    estado = models.CharField(blank=True, max_length=100)
    cidade = models.CharField(blank=True, max_length=100)
    pais = models.CharField(blank=True, max_length=100)
    # metadata
    criado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now_add=True, verbose_name="Criado")
    atualizado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now=True, verbose_name="Atualizado")        
