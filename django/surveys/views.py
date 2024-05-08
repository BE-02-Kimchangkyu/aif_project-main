from rest_framework import generics, viewsets
from .models import SurveyQuestion, SurveyAnswer
from .serializers import SurveyQuestionSerializer, SurveyAnswerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class SurveyQuestionList(generics.ListCreateAPIView):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer


class SurveyQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer


class SurveyAnswerList(generics.ListCreateAPIView):
    queryset = SurveyAnswer.objects.all()
    serializer_class = SurveyAnswerSerializer


class SurveyAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SurveyAnswer.objects.all()
    serializer_class = SurveyAnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer


def save_survey_answer(request, pk):
    survey = get_object_or_404(SurveyQuestion, pk=pk)
    # Logic to save survey answer
    return Response({"message": "Survey answer saved successfully"})


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the surveys index.")


def survey_detail(request, pk):
    return HttpResponse("This is the detail view for survey with id %s." % pk)
