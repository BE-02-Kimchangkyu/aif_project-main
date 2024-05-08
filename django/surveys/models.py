from django.db import models
from django.utils import timezone


class SurveyQuestion(models.Model):
    question_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Survey_Question"

    def __str__(self):
        return self.question_content


class SurveyAnswer(models.Model):
    survey = models.ForeignKey(
        SurveyQuestion, related_name="answers", on_delete=models.CASCADE
    )
    member_id = models.CharField(max_length=100)
    answer_choice = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Survey_Answer"

    def __str__(self):
        return self.member_id
