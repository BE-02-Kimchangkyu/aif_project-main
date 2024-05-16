from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Question"

    def __str__(self):
        return self.question_content


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE
    )
    member_id = models.CharField(max_length=100)
    answer_content = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Answer"

    def __str__(self):
        return self.member_id


class User(models.Model):
    member_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.member_id
