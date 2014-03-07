# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'OportunidadeDeTrabalho.instituicao'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'instituicao_id')

        # Adding field 'OportunidadeDeTrabalho.nome_responsavel'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'nome_responsavel',
                      self.gf('django.db.models.fields.CharField')(default='nome', max_length=100),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.sobre_nome_responsavel'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'sobre_nome_responsavel',
                      self.gf('django.db.models.fields.CharField')(default='nome', max_length=100),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.email_responsavel'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'email_responsavel',
                      self.gf('django.db.models.fields.EmailField')(default='duda@duda.com.br', max_length=75),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.telefone'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'telefone',
                      self.gf('django.db.models.fields.CharField')(default='telefone', max_length=100),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.descricao'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'descricao',
                      self.gf('django.db.models.fields.TextField')(default='desc'),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.descricao_funcional'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'descricao_funcional',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.conhecimento_tecnico'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'conhecimento_tecnico',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.carga_horaria'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'carga_horaria',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.salario_mensal'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'salario_mensal',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.faixa_salarial'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'faixa_salarial',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.beneficios'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'beneficios',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'OportunidadeDeTrabalho.local_de_trabalho'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'local_de_trabalho',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding M2M table for field cargos_e_areas_vinculados on 'OportunidadeDeTrabalho'
        m2m_table_name = db.shorten_name(u'oportunidades_oportunidadedetrabalho_cargos_e_areas_vinculados')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('oportunidadedetrabalho', models.ForeignKey(orm[u'oportunidades.oportunidadedetrabalho'], null=False)),
            ('cargosareaspretendidas', models.ForeignKey(orm[u'profissionais.cargosareaspretendidas'], null=False))
        ))
        db.create_unique(m2m_table_name, ['oportunidadedetrabalho_id', 'cargosareaspretendidas_id'])


        # Changing field 'OportunidadeDeTrabalho.titulo'
        db.alter_column(u'oportunidades_oportunidadedetrabalho', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=300))

    def backwards(self, orm):
        # Adding field 'OportunidadeDeTrabalho.instituicao'
        db.add_column(u'oportunidades_oportunidadedetrabalho', 'instituicao',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['empregadores.Instituicao']),
                      keep_default=False)

        # Deleting field 'OportunidadeDeTrabalho.nome_responsavel'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'nome_responsavel')

        # Deleting field 'OportunidadeDeTrabalho.sobre_nome_responsavel'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'sobre_nome_responsavel')

        # Deleting field 'OportunidadeDeTrabalho.email_responsavel'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'email_responsavel')

        # Deleting field 'OportunidadeDeTrabalho.telefone'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'telefone')

        # Deleting field 'OportunidadeDeTrabalho.descricao'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'descricao')

        # Deleting field 'OportunidadeDeTrabalho.descricao_funcional'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'descricao_funcional')

        # Deleting field 'OportunidadeDeTrabalho.conhecimento_tecnico'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'conhecimento_tecnico')

        # Deleting field 'OportunidadeDeTrabalho.carga_horaria'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'carga_horaria')

        # Deleting field 'OportunidadeDeTrabalho.salario_mensal'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'salario_mensal')

        # Deleting field 'OportunidadeDeTrabalho.faixa_salarial'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'faixa_salarial')

        # Deleting field 'OportunidadeDeTrabalho.beneficios'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'beneficios')

        # Deleting field 'OportunidadeDeTrabalho.local_de_trabalho'
        db.delete_column(u'oportunidades_oportunidadedetrabalho', 'local_de_trabalho')

        # Removing M2M table for field cargos_e_areas_vinculados on 'OportunidadeDeTrabalho'
        db.delete_table(db.shorten_name(u'oportunidades_oportunidadedetrabalho_cargos_e_areas_vinculados'))


        # Changing field 'OportunidadeDeTrabalho.titulo'
        db.alter_column(u'oportunidades_oportunidadedetrabalho', 'titulo', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'beneficios': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'carga_horaria': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cargos_e_areas_vinculados': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profissionais.CargosAreasPretendidas']", 'symmetrical': 'False'}),
            'conhecimento_tecnico': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'criado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'descricao_funcional': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_responsavel': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'empregador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['empregadores.Empregador']"}),
            'faixa_salarial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_de_trabalho': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salario_mensal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'sobre_nome_responsavel': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oportunidades.TipoOportunidadeTrabalho']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '300'})
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
        u'profissionais.curso': {
            'Meta': {'object_name': 'Curso'},
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
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'complemento': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'criado': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'curriculo_arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profissionais.Curso']"}),
            'data_nascimento': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 7, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'formacao_e_cursos_adicionais': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mini_curriculo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'objetivo_profissional': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'outras_experiencias': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
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