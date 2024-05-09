from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    QuestionViewSet,
    SurveyQuestionList,
    SurveyQuestionDetail,
    SurveyAnswerList,
    SurveyAnswerDetail,
    SurveyCheckView,
    SurveyAnswerManageView,
    SurveyStatsManageView,
)

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("", views.SurveyQuestionList.as_view(), name="home"),
    path("survey/<int:pk>/", views.survey_detail, name="survey_detail"),
    path("answer/<int:pk>/", views.save_survey_answer, name="save_survey_answer"),
    path("questions/", SurveyQuestionList.as_view(), name="question_list"),
    path("questions/<int:pk>/", SurveyQuestionDetail.as_view(), name="question_detail"),
    path("answers/", SurveyAnswerList.as_view(), name="answer_list"),
    path("answers/<int:pk>/", SurveyAnswerDetail.as_view(), name="answer_detail"),
    path("", include(router.urls)),
    path(
        "image/<str:member_id>/survey", SurveyCheckView.as_view(), name="survey-check"
    ),
    path(
        "aif/manage/surveyanswer",
        SurveyAnswerManageView.as_view(),
        name="survey-answer-manage",
    ),
    path(
        "aif/manage/surveystats",
        SurveyStatsManageView.as_view(),
        name="survey-stats-manage",
    ),
]
