from django.test import TestCase
from .models import SurveyQuestion, SurveyAnswer


class SurveyQuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SurveyQuestion.objects.create(question_content="test question")

    def test_question_content_label(self):
        surveyquestion = SurveyQuestion.objects.get(id=1)
        field_label = surveyquestion._meta.get_field("question_content").verbose_name
        self.assertEqual(field_label, "question content")


class SurveyAnswerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SurveyAnswer.objects.create(survey_id=1, member_id=1, answer_choice="A")

    def test_answer_choice_label(self):
        surveyanswer = SurveyAnswer.objects.get(id=1)
        field_label = surveyanswer._meta.get_field("answer_choice").verbose_name
        self.assertEqual(field_label, "answer choice")
