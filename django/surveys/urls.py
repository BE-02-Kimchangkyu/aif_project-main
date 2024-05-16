from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    Questions,
    QuestionDetail,
    Answers,
    AnswersByUser,
    AnswersByQuestion,
)
from . import views

router = DefaultRouter()

urlpatterns = [
    path("questions/", Questions.as_view(), name="questions"),
    path(
        "questions/<int:question_id>/", QuestionDetail.as_view(), name="question_detail"
    ),
    path("answers/", Answers.as_view(), name="answers"),
    path(
        "answers/user/<int:member_id>/", AnswersByUser.as_view(), name="answers_by_user"
    ),
    path(
        "answers/question/<int:question_id>/",
        AnswersByQuestion.as_view(),
        name="answers_by_question",
    ),
    path("", views.surveys_index, name="surveys_index"),
]
