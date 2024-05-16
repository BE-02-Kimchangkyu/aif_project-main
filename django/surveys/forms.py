from django import forms
from .models import Question, Answer, User


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_content"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["question", "member_id", "answer_content"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["member_id"]
