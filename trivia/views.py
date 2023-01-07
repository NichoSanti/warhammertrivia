from trivia.models import TrueOrFalse
from trivia.serializers import QuestionSerializer
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = TrueOrFalse.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrueOrFalse.objects.all()
    serializer_class = QuestionSerializer
