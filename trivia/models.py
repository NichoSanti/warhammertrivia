from django.db import models

class TrueOrFalse(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    question = models.TextField(max_length=500)
    answer = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ['created']
        
