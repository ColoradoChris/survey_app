from django.contrib import admin
from .models import Survey, SurveyQuestion, SurveyChoice
# Register your models here.

class QuestionInLine(admin.TabularInline):
    model = SurveyQuestion
    extra = 1

class ChoiceInLine(admin.TabularInline):
    model = SurveyChoice
    extra = 2

class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Questions',               {'fields': ['name']}),
        ]
    inlines = [QuestionInLine, ChoiceInLine]
    search_fields = ['question_text']

admin.site.register(Survey, SurveyAdmin)
