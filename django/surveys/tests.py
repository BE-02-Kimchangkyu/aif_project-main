from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Question, Answer, User


class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Question.objects.create(question_content="test question")

    def test_question_content_label(self):
        question = Question.objects.get(id=1)
        field_label = question._meta.get_field("question_content").verbose_name
        self.assertEqual(field_label, "question content")


class AnswerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(member_id="1")
        question = Question.objects.create(question_content="test question")
        Answer.objects.create(user=user, question=question, answer_content="A")

    def test_answer_content_label(self):
        answer = Answer.objects.get(id=1)
        field_label = answer._meta.get_field("answer_content").verbose_name
        self.assertEqual(field_label, "answer content")


class QuestionAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_questions(self):
        response = self.client.get(reverse("questions"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AnswerAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_answers(self):
        response = self.client.get(reverse("answers"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
