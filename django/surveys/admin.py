from django.contrib import admin
from .models import Survey, Question, Choice, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 7


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 7


class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Answer)
