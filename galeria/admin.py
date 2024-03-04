from django.contrib import admin
from galeria.models import Fotografia


@admin.register(Fotografia)
class ListandoFotografias(admin.ModelAdmin):
    # ordering = ['id']
    list_display = ('id', 'publicada', 'nome', 'legenda', 'foto')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'descricao',)  # também pode ser uma lista ['nome']
    list_filter = ['categoria', 'publicada']
    list_editable = ['publicada']
    list_per_page = 10
    search_help_text = 'Pesquisa em nome e descrição das fotografias'


# admin.site.register(Fotografia, ListandoFotografias)
