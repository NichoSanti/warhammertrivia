from django.db import models
# class TrueOrFalse(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     question = models.TextField(max_length=500)
#     answer = models.CharField(max_length=50, default='')

#     class Meta:
#         ordering = ['created']

class Question(models.Model):
    title = models.CharField('title', max_length=255)
    points = models.SmallIntegerField('points')
    is_active = models.BooleanField('Is Active', default=True)
    created_at = models.DateTimeField('Created', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True, auto_now_add=False)

def __str__(self) -> str:
    return self.title
    
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', verbose_name=("Question"), on_delete=models.CASCADE)
    answer = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)
    is_active = models.BooleanField('Is Active', default=True)
    created_at = models.DateTimeField('Created', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True, auto_now_add=False)

def __str__(self) -> str:
    return self.answer

    
        
