# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaisdoProfissional'
        db.create_table(u'profissionais_paisdoprofissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['PaisdoProfissional'])

        # Adding model 'CidadedoProfissional'
        db.create_table(u'profissionais_cidadedoprofissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.EstadoProfissional'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['CidadedoProfissional'])

        # Adding model 'EstadoProfissional'
        db.create_table(u'profissionais_estadoprofissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['EstadoProfissional'])

        # Adding model 'CargosAreasPretendidas'
        db.create_table(u'profissionais_cargosareaspretendidas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['CargosAreasPretendidas'])

        # Adding model 'Profissional'
        db.create_table(u'profissionais_profissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('curso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Curso'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('sobrenome', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('curriculo_arquivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('possui_filhos', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_nascimento', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 6, 0, 0))),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.PaisdoProfissional'])),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('complemento', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.EstadoProfissional'])),
            ('cidade', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.CidadedoProfissional'])),
            ('telefone_residencial', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('telefone_comercial', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('telefone_celular', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('portador_de_deficiencia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('objetivo_profissional', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('mini_curriculo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('aceita_trabalho_temporario', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('formacao_e_cursos_adicionais', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('outras_experiencias', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('criado', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('atualizado', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['Profissional'])

        # Adding M2M table for field cargos_e_areas_pretendidas on 'Profissional'
        m2m_table_name = db.shorten_name(u'profissionais_profissional_cargos_e_areas_pretendidas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profissional', models.ForeignKey(orm[u'profissionais.profissional'], null=False)),
            ('cargosareaspretendidas', models.ForeignKey(orm[u'profissionais.cargosareaspretendidas'], null=False))
        ))
        db.create_unique(m2m_table_name, ['profissional_id', 'cargosareaspretendidas_id'])

        # Adding model 'Idioma'
        db.create_table(u'profissionais_idioma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['Idioma'])

        # Adding model 'IdiomasdoProfissional'
        db.create_table(u'profissionais_idiomasdoprofissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profissional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Profissional'])),
            ('idioma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Idioma'])),
            ('nivel', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['IdiomasdoProfissional'])

        # Adding model 'FormacaoAcademicaDoProfissional'
        db.create_table(u'profissionais_formacaoacademicadoprofissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profissional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Profissional'])),
            ('grau', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('instituicao', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('nome_do_curso', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('data_inicio', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 6, 0, 0))),
            ('data_conclusao', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['FormacaoAcademicaDoProfissional'])

        # Adding model 'ExperienciaDoProfissional'
        db.create_table(u'profissionais_experienciadoprofissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profissional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Profissional'])),
            ('empresa', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('data_inicio', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 6, 0, 0))),
            ('data_conclusao', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('salario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('funcoes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profissionais', ['ExperienciaDoProfissional'])

        # Adding model 'CertificacaoDoProfissional'
        db.create_table(u'profissionais_certificacaodoprofissional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profissional', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profissionais.Profissional'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['CertificacaoDoProfissional'])

        # Adding model 'Curso'
        db.create_table(u'profissionais_curso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'profissionais', ['Curso'])


    def backwards(self, orm):
        # Deleting model 'PaisdoProfissional'
        db.delete_table(u'profissionais_paisdoprofissional')

        # Deleting model 'CidadedoProfissional'
        db.delete_table(u'profissionais_cidadedoprofissional')

        # Deleting model 'EstadoProfissional'
        db.delete_table(u'profissionais_estadoprofissional')

        # Deleting model 'CargosAreasPretendidas'
        db.delete_table(u'profissionais_cargosareaspretendidas')

        # Deleting model 'Profissional'
        db.delete_table(u'profissionais_profissional')

        # Removing M2M table for field cargos_e_areas_pretendidas on 'Profissional'
        db.delete_table(db.shorten_name(u'profissionais_profissional_cargos_e_areas_pretendidas'))

        # Deleting model 'Idioma'
        db.delete_table(u'profissionais_idioma')

        # Deleting model 'IdiomasdoProfissional'
        db.delete_table(u'profissionais_idiomasdoprofissional')

        # Deleting model 'FormacaoAcademicaDoProfissional'
        db.delete_table(u'profissionais_formacaoacademicadoprofissional')

        # Deleting model 'ExperienciaDoProfissional'
        db.delete_table(u'profissionais_experienciadoprofissional')

        # Deleting model 'CertificacaoDoProfissional'
        db.delete_table(u'profissionais_certificacaodoprofissional')

        # Deleting model 'Curso'
        db.delete_table(u'profissionais_curso')


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
        u'profissionais.cargosareaspretendidas': {
            'Meta': {'object_name': 'CargosAreasPretendidas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'profissionais.certificacaodoprofissional': {
            'Meta': {'object_name': 'CertificacaoDoProfissional'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"})
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
        u'profissionais.experienciadoprofissional': {
            'Meta': {'object_name': 'ExperienciaDoProfissional'},
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'data_conclusao': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'data_inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 6, 0, 0)'}),
            'empresa': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'funcoes': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"}),
            'salario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'profissionais.formacaoacademicadoprofissional': {
            'Meta': {'object_name': 'FormacaoAcademicaDoProfissional'},
            'data_conclusao': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'data_inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 6, 0, 0)'}),
            'grau': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instituicao': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'nome_do_curso': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"})
        },
        u'profissionais.idioma': {
            'Meta': {'object_name': 'Idioma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'profissionais.idiomasdoprofissional': {
            'Meta': {'object_name': 'IdiomasdoProfissional'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Idioma']"}),
            'nivel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'profissional': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Profissional']"})
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

    complete_apps = ['profissionais']