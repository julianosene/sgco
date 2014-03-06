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


SEXO_CHOICES = (
    ('m', 'Masculino'),
    ('f', 'Feminino'),
)


ESTADO_CIVIL_CHOICES = (
    ('solteiro', 'Solteiro'),
    ('casado', 'Casado'),
    ('separado', 'Separado'),
    ('divorcidado', 'Divorciado'),
    ('viuvo', 'Viúvo'),
    ('outro', 'Outro'),
)


GRAU_CHOICES = (
    ('ensino_medio', 'Ensino Médio'),
    ('tecnico', 'Técnico'),
    ('graduacao', 'Graduação'),
    ('pos', 'Pós Graduação'),
    ('mba', 'MBA'),
    ('mestrado', 'Mestrado'),
    ('doutorado', 'Doutorado'),
    ('phd', 'Pós Doutorado'),
    ('livre', 'Livre Docência'),
    ('tecnologo', 'Tecnólogo'),
)

SALARIO_CHOICES = (
    ('faixa1', 'Até R$1.000 por mês'),
    ('faixa2', 'De R$1.001 a R$2.000 por mês'),
    ('faixa3', 'De R$2.001 a R$4.000 por mês'),
    ('faixa4', 'De R$4.001 a R$8.000 por mês'),
    ('faixa5', 'Acima de R$8.000 por mês'),
)

NIVEL_IDIOMA_CHOICES = (
    ('basico', 'Básico'),
    ('intermediario', 'Intermediário'),
    ('avancado', 'Avançado'),
    ('fluente', 'Fluente'),
)


class PaisdoProfissional(models.Model):
    
    def __unicode__(self):
        return self.nome
        
    nome = models.CharField(blank=True, max_length=100)


class CidadedoProfissional(models.Model):
    
    def __unicode__(self):
        return self.nome
        
    estado = models.ForeignKey("EstadoProfissional")
    nome = models.CharField(blank=True, max_length=100)

class EstadoProfissional(models.Model):
    
    def __unicode__(self):
        return self.nome
    
    pais = models.ForeignKey('PaisdoProfissional')
    nome = models.CharField(blank=True, max_length=100)


class CargosAreasPretendidas(models.Model):
    
    def __unicode__(self):
        return self.nome
        
    nome = models.CharField(blank=True, max_length=200)
    

class Profissional(models.Model):
    
    def __unicode__(self):
        return "Nome: %s" % self.nome
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuário do Sistema", blank=True, null=True)
    uuid = UUIDField()
    curso = models.ForeignKey("Curso")
    foto = models.ImageField(upload_to=profissional_foto_path, blank=False)
    nome = models.CharField(blank=False, max_length=500)
    sobrenome = models.CharField(blank=False, max_length=500)
    email = models.EmailField()
    curriculo_arquivo = models.FileField(upload_to=profissional_curriculo_path)
    sexo = models.CharField(blank=True, max_length=1, choices=SEXO_CHOICES)
    estado_civil = models.CharField(blank=True, max_length=100, choices=ESTADO_CIVIL_CHOICES)
    possui_filhos = models.BooleanField(default=False)
    data_nascimento = models.DateField(default=datetime.datetime.today)
    pais = models.ForeignKey('PaisdoProfissional')
    # endereco
    endereco = models.CharField(blank=True, max_length=500)
    numero = models.CharField(blank=True, max_length=100)
    complemento = models.CharField(blank=True, max_length=100)
    bairro = models.CharField(blank=True, max_length=100)
    cep = models.CharField(blank=True, max_length=100)
    estado = models.ForeignKey("EstadoProfissional")
    cidade = models.ForeignKey("CidadedoProfissional")
    # contatos
    telefone_residencial = models.CharField(blank=True, max_length=100)
    telefone_comercial = models.CharField(blank=True, max_length=100)
    telefone_celular = models.CharField(blank=True, max_length=100)
    # outros
    portador_de_deficiencia = models.BooleanField(default=False)
    # Curriculo
    objetivo_profissional = models.TextField(blank=True)
    cargos_e_areas_pretendidas = models.ManyToManyField("CargosAreasPretendidas")
    mini_curriculo = models.TextField(blank=True)
    aceita_trabalho_temporario = models.BooleanField(default=False)
    # Formacao / Cursos Adicionais
    formacao_e_cursos_adicionais = models.TextField(blank=True)
    outras_experiencias = models.TextField(blank=True)
    # metadata
    criado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now_add=True, verbose_name="Criado")
    atualizado = models.DateTimeField(blank=True, default=datetime.datetime.now, auto_now=True, verbose_name="Atualizado")        

class Idioma(models.Model):
    nome = models.CharField(blank=True, max_length=100)

class IdiomasdoProfissional(models.Model):
    profissional = models.ForeignKey("Profissional")
    idioma = models.ForeignKey("Idioma")
    nivel = models.CharField(blank=True, max_length=100, choices=NIVEL_IDIOMA_CHOICES)

class FormacaoAcademicaDoProfissional(models.Model):
    
    profissional = models.ForeignKey("Profissional")
    grau = models.CharField(blank=True, max_length=100, choices=GRAU_CHOICES)
    instituicao = models.CharField(blank=True, max_length=200)
    nome_do_curso = models.CharField(blank=True, max_length=200)
    data_inicio = models.DateField(default=datetime.datetime.today)
    data_conclusao = models.DateField(blank=True)


class ExperienciaDoProfissional(models.Model):
    
    profissional = models.ForeignKey("Profissional")
    empresa = models.CharField(blank=False, max_length=500)
    cargo = models.CharField(blank=False, max_length=500)
    data_inicio = models.DateField(default=datetime.datetime.today)
    data_conclusao = models.DateField(blank=True)
    salario = models.CharField(blank=True, max_length=100, choices=SALARIO_CHOICES)
    funcoes = models.TextField(blank=False)

class CertificacaoDoProfissional(models.Model):
    
    profissional = models.ForeignKey("Profissional")
    nome = models.CharField(blank=True, max_length=200)


class Curso(models.Model):
    
    def __unicode__(self):
        return self.nome
    
    nome = models.CharField(blank=True, max_length=100)