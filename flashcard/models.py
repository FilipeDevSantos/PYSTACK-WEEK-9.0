from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.name
    

class Flashcard(models.Model):
    DIFICULTIES_CHOICES = (('D', 'Difícil'), ('M', 'Médio'), ('F', 'Fácil'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length = 100)
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    dificulty = models.CharField(max_length=1, choices=DIFICULTIES_CHOICES)

    def __str__(self) -> str:
        return self.question