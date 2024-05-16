from rest_framework import serializers
from .models import Question, Answer, User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_content", "created_at", "modified_at"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "question",
            "member_id",
            "answer_content",
            "created_at",
            "modified_at",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["member_id", "created_at", "modified_at"]
