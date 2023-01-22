from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from trivia import views

urlpatterns = [
    path('trivia/random/', views.RandomQuestion.as_view(), name='random'),
]

