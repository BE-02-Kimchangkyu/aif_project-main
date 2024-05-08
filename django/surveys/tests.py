from django.test import TestCase
from .models import Survey, Question, Answer


class SurveyModelTest(TestCase):
    def test_string_representation(self):
        survey = Survey(title="My Survey")
        self.assertEqual(str(survey), survey.title)


class QuestionModelTest(TestCase):
    def test_string_representation(self):
        question = Question(text="My Question")
        self.assertEqual(str(question), question.text)


class AnswerModelTest(TestCase):
    def test_string_representation(self):
        answer = Answer(text="My Answer")
        self.assertEqual(str(answer), answer.text)


class SurveyChoiceTest(TestCase):
    def test_string_representation(self):
        choice = Choice(text="My Choice")
        self.assertEqual(str(choice), choice.text)
