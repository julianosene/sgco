# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Instituicao'
        db.delete_table(u'empregadores_instituicao')

        # Adding model 'RamoEmpregador'
        db.create_table(u'empregadores_ramoempregador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'empregadores', ['RamoEmpregador'])

        # Deleting field 'Empregador.descricao'
        db.delete_column(u'empregadores_empregador', 'descricao')

        # Adding field 'Empregador.historico'
        db.add_column(u'empregadores_empregador', 'historico',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.nome_responsavel'
        db.add_column(u'empregadores_empregador', 'nome_responsavel',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.sobre_nome_responsavel'
        db.add_column(u'empregadores_empregador', 'sobre_nome_responsavel',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.email_responsavel'
        db.add_column(u'empregadores_empregador', 'email_responsavel',
                      self.gf('django.db.models.fields.EmailField')(default='admin@admin.com', max_length=75),
                      keep_default=False)

        # Adding field 'Empregador.nome_fantasia'
        db.add_column(u'empregadores_empregador', 'nome_fantasia',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.razao_social'
        db.add_column(u'empregadores_empregador', 'razao_social',
                      self.gf('django.db.models.fields.CharField')(default='razao', max_length=100),
                      keep_default=False)

        # Adding field 'Empregador.ramo'
        db.add_column(u'empregadores_empregador', 'ramo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['empregadores.RamoEmpregador']),
                      keep_default=False)

        # Adding field 'Empregador.cnpj'
        db.add_column(u'empregadores_empregador', 'cnpj',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.endereco'
        db.add_column(u'empregadores_empregador', 'endereco',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.numero'
        db.add_column(u'empregadores_empregador', 'numero',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.complemento'
        db.add_column(u'empregadores_empregador', 'complemento',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.bairro'
        db.add_column(u'empregadores_empregador', 'bairro',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.cep'
        db.add_column(u'empregadores_empregador', 'cep',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.estado'
        db.add_column(u'empregadores_empregador', 'estado',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.cidade'
        db.add_column(u'empregadores_empregador', 'cidade',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Empregador.pais'
        db.add_column(u'empregadores_empregador', 'pais',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Instituicao'
        db.create_table(u'empregadores_instituicao', (
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'empregadores', ['Instituicao'])

        # Deleting model 'RamoEmpregador'
        db.delete_table(u'empregadores_ramoempregador')

        # Adding field 'Empregador.descricao'
        db.add_column(u'empregadores_empregador', 'descricao',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Deleting field 'Empregador.historico'
        db.delete_column(u'empregadores_empregador', 'historico')

        # Deleting field 'Empregador.nome_responsavel'
        db.delete_column(u'empregadores_empregador', 'nome_responsavel')

        # Deleting field 'Empregador.sobre_nome_responsavel'
        db.delete_column(u'empregadores_empregador', 'sobre_nome_responsavel')

        # Deleting field 'Empregador.email_responsavel'
        db.delete_column(u'empregadores_empregador', 'email_responsavel')

        # Deleting field 'Empregador.nome_fantasia'
        db.delete_column(u'empregadores_empregador', 'nome_fantasia')

        # Deleting field 'Empregador.razao_social'
        db.delete_column(u'empregadores_empregador', 'razao_social')

        # Deleting field 'Empregador.ramo'
        db.delete_column(u'empregadores_empregador', 'ramo_id')

        # Deleting field 'Empregador.cnpj'
        db.delete_column(u'empregadores_empregador', 'cnpj')

        # Deleting field 'Empregador.endereco'
        db.delete_column(u'empregadores_empregador', 'endereco')

        # Deleting field 'Empregador.numero'
        db.delete_column(u'empregadores_empregador', 'numero')

        # Deleting field 'Empregador.complemento'
        db.delete_column(u'empregadores_empregador', 'complemento')

        # Deleting field 'Empregador.bairro'
        db.delete_column(u'empregadores_empregador', 'bairro')

        # Deleting field 'Empregador.cep'
        db.delete_column(u'empregadores_empregador', 'cep')

        # Deleting field 'Empregador.estado'
        db.delete_column(u'empregadores_empregador', 'estado')

        # Deleting field 'Empregador.cidade'
        db.delete_column(u'empregadores_empregador', 'cidade')

        # Deleting field 'Empregador.pais'
        db.delete_column(u'empregadores_empregador', 'pais')


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
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'criado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'email_responsavel': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'historico': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nome_fantasia': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ramo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empregadores.RamoEmpregador']"}),
            'razao_social': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sobre_nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'})
        },
        u'empregadores.ramoempregador': {
            'Meta': {'object_name': 'RamoEmpregador'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['empregadores']