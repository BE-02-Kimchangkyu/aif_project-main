from rest_framework import serializers
from .models import SurveyQuestion, SurveyAnswer


class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = ["id", "question_content", "created_at", "modified_at"]


class SurveyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = [
            "id",
            "survey",
            "member_id",
            "answer_choice",
            "created_at",
            "modified_at",
        ]
