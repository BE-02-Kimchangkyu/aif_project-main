from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("", views.survey_list, name="survey_list"),
    path("survey/<int:pk>/", views.survey_detail, name="survey_detail"),
    path("answer/<int:pk>/", views.save_survey_answer, name="save_survey_answer"),
    path("", include(router.urls)),
]
