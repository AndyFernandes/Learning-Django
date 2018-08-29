from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

# Ai parece que tem um monte de propriedades nesses negócios
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question_text']}),
			('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
			]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently') # aqui mostra o que vai ter no display, ai a gente modificou um negocio no model até
	list_filter = ['pub_date'] # habilita um filtro na lateral direita que se adequa a aquilo que está ordenando
	search_fields = ['question_text'] # habilita o negócio de pesquisa



admin.site.register(Question, QuestionAdmin)

