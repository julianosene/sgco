# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OportunidadeDeTrabalho'
        db.create_table(u'oportunidades_oportunidadedetrabalho', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empregador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empregadores.Empregador'])),
            ('instituicao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empregadores.Instituicao'])),
            ('ativa', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oportunidades.TipoOportunidadeTrabalho'])),
            ('criado', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('atualizado', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'oportunidades', ['OportunidadeDeTrabalho'])

        # Adding model 'InscricaoOportunidade'
        db.create_table(u'oportunidades_inscricaooportunidade', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('oportunidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oportunidades.OportunidadeDeTrabalho'])),
            ('profissional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Profissional'])),
            ('criado', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('atualizado', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'oportunidades', ['InscricaoOportunidade'])

        # Adding unique constraint on 'InscricaoOportunidade', fields ['oportunidade', 'profissional']
        db.create_unique(u'oportunidades_inscricaooportunidade', ['oportunidade_id', 'profissional_id'])

        # Adding model 'TipoOportunidadeTrabalho'
        db.create_table(u'oportunidades_tipooportunidadetrabalho', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'oportunidades', ['TipoOportunidadeTrabalho'])


    def backwards(self, orm):
        # Removing unique constraint on 'InscricaoOportunidade', fields ['oportunidade', 'profissional']
        db.delete_unique(u'oportunidades_inscricaooportunidade', ['oportunidade_id', 'profissional_id'])

        # Deleting model 'OportunidadeDeTrabalho'
        db.delete_table(u'oportunidades_oportunidadedetrabalho')

        # Deleting model 'InscricaoOportunidade'
        db.delete_table(u'oportunidades_inscricaooportunidade')

        # Deleting model 'TipoOportunidadeTrabalho'
        db.delete_table(u'oportunidades_tipooportunidadetrabalho')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'empregadores.empregador': {
            'Meta': {'object_name': 'Empregador'},
            'atualizado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'criado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'empregadores.instituicao': {
            'Meta': {'object_name': 'Instituicao'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'oportunidades.inscricaooportunidade': {
            'Meta': {'unique_together': "(('oportunidade', 'profissional'),)", 'object_name': 'InscricaoOportunidade'},
            'atualizado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'criado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oportunidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oportunidades.OportunidadeDeTrabalho']"}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"})
        },
        u'oportunidades.oportunidadedetrabalho': {
            'Meta': {'object_name': 'OportunidadeDeTrabalho'},
            'ativa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'atualizado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'criado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'empregador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empregadores.Empregador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituicao': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empregadores.Instituicao']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oportunidades.TipoOportunidadeTrabalho']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'oportunidades.tipooportunidadetrabalho': {
            'Meta': {'object_name': 'TipoOportunidadeTrabalho'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'profissionais.cargosareaspretendidas': {
            'Meta': {'object_name': 'CargosAreasPretendidas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'profissionais.cidadedoprofissional': {
            'Meta': {'object_name': 'CidadedoProfissional'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.EstadoProfissional']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'profissionais.curso': {
            'Meta': {'object_name': 'Curso'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'profissionais.estadoprofissional': {
            'Meta': {'object_name': 'EstadoProfissional'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'profissionais.paisdoprofissional': {
            'Meta': {'object_name': 'PaisdoProfissional'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'profissionais.profissional': {
            'Meta': {'object_name': 'Profissional'},
            'aceita_trabalho_temporario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'atualizado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cargos_e_areas_pretendidas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profissionais.CargosAreasPretendidas']", 'symmetrical': 'False'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cidade': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.CidadedoProfissional']"}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'criado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'curriculo_arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Curso']"}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 6, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.EstadoProfissional']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'formacao_e_cursos_adicionais': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mini_curriculo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'objetivo_profissional': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'outras_experiencias': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.PaisdoProfissional']"}),
            'portador_de_deficiencia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'possui_filhos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'sobrenome': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'telefone_celular': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'telefone_comercial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'telefone_residencial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        }
    }

    complete_apps = ['oportunidades']