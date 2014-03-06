# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

import datetime

# Create your models here.

class OportunidadeDeTrabalho(models.Model):
    
    def __unicode__(self):
        
        return "Oportunidade de Trabalho: %s em %s" % (self.titulo, self.empregador)
    
    empregador = models.ForeignKey("empregadores.Empregador")
    ativa = models.BooleanField(default=True)
    titulo = models.CharField(blank=True, max_length=100)
    # metadata
    criado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now_add=True, verbose_name="Criado")
    atualizado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now=True, verbose_name="Atualizado")

class InscricaoOportunidade(models.Model):
    
    oportunidade = models.ForeignKey("OportunidadeDeTrabalho")
    profissional = models.ForeignKey('profissionais.Profissional')
    # metadata
    criado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now_add=True, verbose_name="Criado")
    atualizado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now=True, verbose_name="Atualizado")

    class Meta:
        unique_together = (('oportunidade', 'profissional'),)