from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date
from django.db.models import Q
from .models import SurveyQuestion, SurveyAnswer
from .serializers import SurveyQuestionSerializer, SurveyAnswerSerializer


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


@api_view(["POST"])
def save_survey_answer(request, pk):
    survey = get_object_or_404(SurveyQuestion, pk=pk)
    data = JSONParser().parse(request)
    serializer = SurveyAnswerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Survey answer saved successfully"})
    return Response(serializer.errors, status=400)


def index(request):
    return HttpResponse("Hello, world. You're at the surveys index.")


def survey_detail(request, pk):
    return HttpResponse("This is the detail view for survey with id %s." % pk)


class SurveyCheckView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, member_id, format=None):
        user = request.user
        if user.email != member_id:
            return JsonResponse({"detail": "Unauthorized"}, status=401)

        survey_done = SurveyAnswer.objects.filter(member_id=member_id).exists()
        return JsonResponse({"survey_done": survey_done})


class SurveyAnswerManageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        survey_answers = SurveyAnswer.objects.filter(member_id=user.email)
        answer_list = [
            {
                "questionId": answer.survey.question_content,
                "answer": answer.answer_choice,
            }
            for answer in survey_answers
        ]
        return JsonResponse({"answer": answer_list})


class SurveyStatsManageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        filter_data = request.data.get("filter", {})
        survey_id = filter_data.get("surveyId", "")
        date_from = parse_date(filter_data.get("dateFrom", ""))
        date_to = parse_date(filter_data.get("dateTo", ""))

        survey_answers = SurveyAnswer.objects.filter(
            Q(survey__id=survey_id) if survey_id else Q(),
            Q(created_at__gte=date_from) if date_from else Q(),
            Q(created_at__lte=date_to) if date_to else Q(),
        )

        # Convert survey_answers to the desired format
        serializer = SurveyAnswerSerializer(survey_answers, many=True)
        data = serializer.data

        return JsonResponse(
            {
                "success": True,
                "code": 200,
                "message": "설문 불러오기 성공",
                "data": data,
            }
        )
