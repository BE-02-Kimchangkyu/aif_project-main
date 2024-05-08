from django import forms
from .models import SurveyAnswer, SurveyQuestion


class SurveyAnswerForm(forms.ModelForm):
    class Meta:
        model = SurveyAnswer
        fields = ["question_content"]


class SurveyQuestionForm(forms.ModelForm):
    class Meta:
        model = SurveyQuestion
        fields = ["survey", "member_id", "answer_choice"]
