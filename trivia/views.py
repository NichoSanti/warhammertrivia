from trivia.models import TrueOrFalse
from trivia.serializers import QuestionSerializer
from rest_framework import generics
import random


class QuestionList(generics.ListCreateAPIView):
    queryset = TrueOrFalse.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrueOrFalse.objects.all()
    serializer_class = QuestionSerializer

class RandomQuestion(generics.ListAPIView):
    queryset = TrueOrFalse.objects.order_by('?')[:1]
    serializer_class = QuestionSerializer

    
