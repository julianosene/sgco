from django.contrib import admin

from models import Profissional
from models import IdiomasdoProfissional
from models import Idioma
from models import FormacaoAcademicaDoProfissional
from models import ExperienciaDoProfissional
from models import CertificacaoDoProfissional
from models import Curso
from models import CargosAreasPretendidas

class IdiomasdoProfissionalInline(admin.StackedInline):
    model = IdiomasdoProfissional
    extra = 0

class FormacaoAcademicaDoProfissionalInline(admin.StackedInline):
    model = FormacaoAcademicaDoProfissional
    extra = 0
    
class ExperienciaDoProfissionalInline(admin.StackedInline):
    model = ExperienciaDoProfissional
    extra = 0

class CertificacaoDoProfissionalInline(admin.StackedInline):
    model = CertificacaoDoProfissional
    extra = 0

class ProfissionalAdmin(admin.ModelAdmin):
    
    list_display = 'nome', 'sobrenome', 'email', 'user'
    
    inlines = [
        IdiomasdoProfissionalInline,
        FormacaoAcademicaDoProfissionalInline,
        ExperienciaDoProfissionalInline,
        CertificacaoDoProfissionalInline,
    ]

# Register your models here.
admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(IdiomasdoProfissional)
admin.site.register(Curso)
admin.site.register(CargosAreasPretendidas)
admin.site.register(Idioma)
admin.site.register(FormacaoAcademicaDoProfissional)
admin.site.register(ExperienciaDoProfissional)
admin.site.register(CertificacaoDoProfissional)