from django.contrib import admin
from .models import Question, Answer, User


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class AnswerAdmin(admin.ModelAdmin):
    fields = ["question", "member_id", "answer_content", "created_at", "modified_at"]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


class UserAdmin(admin.ModelAdmin):
    fields = ["member_id", "created_at", "modified_at"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(User, UserAdmin)
