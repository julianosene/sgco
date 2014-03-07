# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

import datetime

SALARIO_CHOICES = (
    ('faixa1', 'Até R$1.000 por mês'),
    ('faixa2', 'De R$1.001 a R$2.000 por mês'),
    ('faixa3', 'De R$2.001 a R$4.000 por mês'),
    ('faixa4', 'De R$4.001 a R$8.000 por mês'),
    ('faixa5', 'Acima de R$8.000 por mês'),
)

# Create your models here.

class OportunidadeDeTrabalho(models.Model):
    
    def __unicode__(self):
        
        return "Oportunidade de Trabalho: %s em %s" % (self.titulo, self.empregador)
    
    empregador = models.ForeignKey("empregadores.Empregador")    
    ativa = models.BooleanField(default=True)
    # DADOS RESPONSAVEL CADASTRO - PUXA DO EMPREGADOR
    nome_responsavel = models.CharField(blank=False, max_length=100)
    sobre_nome_responsavel = models.CharField(blank=False, max_length=100)
    email_responsavel = models.EmailField()
    telefone = models.CharField(blank=False, max_length=100)
    titulo = models.CharField(blank=False, max_length=300)
    tipo = models.ForeignKey("TipoOportunidadeTrabalho")
    cargos_e_areas_vinculados = models.ManyToManyField("profissionais.CargosAreasPretendidas")
    descricao = models.TextField(blank=False)
    descricao_funcional = models.TextField(blank=True)
    conhecimento_tecnico = models.TextField(blank=True)
    carga_horaria = models.TextField(blank=True)
    salario_mensal = models.CharField(blank=True, max_length=100)
    faixa_salarial = models.CharField(blank=True, max_length=100, choices=SALARIO_CHOICES)
    beneficios = models.TextField(blank=True)
    local_de_trabalho = models.TextField(blank=True)
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

class TipoOportunidadeTrabalho(models.Model):
    nome = models.CharField(blank=True, max_length=100)