from django.db import models

class QandAModel(models.Model):
    question = models.CharField(max_length=100, verbose_name='Вопрос')
    answer = models.CharField(max_length=100, verbose_name='Ответ')

    def __str__(self):
        return self.question