from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from trivia import views

urlpatterns = [
    path('trivia/', views.QuestionList.as_view()),
    path('trivia/<int:pk>/', views.QuestionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)