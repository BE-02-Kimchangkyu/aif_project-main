from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer, User
from .forms import AnswerForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionMixin:
    def get_question(self, question_id):
        return get_object_or_404(Question, pk=question_id)


class Questions(APIView):
    # permission_classes = [IsAuthenticated]  # 추가: 인증 설정

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(QuestionMixin, APIView):
    def get(self, request, question_id):
        question = self.get_question(question_id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, question_id):
        question = self.get_question(question_id)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            answer = serializer.save(user=request.user, question=question)
            serializer = AnswerSerializer(answer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Answers(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


class AnswersByUser(APIView):
    def get_answers_by_user(self, member_id):
        user = get_object_or_404(User, member_id=member_id)
        return Answer.objects.filter(user=user)

    def get(self, request, member_id):
        answers = self.get_answers_by_user(member_id)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswersByQuestion(QuestionMixin, APIView):
    def get_answers_by_question(self, question_id):
        question = self.get_question(question_id)
        return Answer.objects.filter(question=question)

    def get(self, request, question_id):
        answers = self.get_answers_by_question(question_id)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, question_id):
        question = self.get_question(question_id)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            answer = serializer.save(user=request.user, question=question)
            serializer = AnswerSerializer(answer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.http import HttpResponse


def other_view(request):
    return HttpResponse("Hello, world!")


def surveys_index(request):
    return HttpResponse("Hello, this is the surveys index.")
