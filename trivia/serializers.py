from rest_framework import serializers
from trivia.models import TrueOrFalse

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrueOrFalse 
        fields = ['id', 'question', 'answer']


