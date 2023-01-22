from django.contrib import admin
from . import models

class AnswerInline(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer',
        'is_correct',
    ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'points',
    ]
    list_display = [
        'title',
        'points',
    ]
    inlines = [
        AnswerInline,
    ]

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer',
        'is_correct',
        'question',
    ]