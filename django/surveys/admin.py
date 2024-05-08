from django.contrib import admin
from .models import SurveyQuestion, SurveyAnswer


class SurveyAnswerInline(admin.TabularInline):
    model = SurveyAnswer
    extra = 7


class SurveyQuestionAdmin(admin.ModelAdmin):
    inlines = [SurveyAnswerInline]


admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(SurveyAnswer)
