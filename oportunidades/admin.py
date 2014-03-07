from django.contrib import admin

from models import OportunidadeDeTrabalho
from models import InscricaoOportunidade
from models import TipoOportunidadeTrabalho


# Register your models here.
admin.site.register(OportunidadeDeTrabalho)
admin.site.register(InscricaoOportunidade)
admin.site.register(TipoOportunidadeTrabalho)