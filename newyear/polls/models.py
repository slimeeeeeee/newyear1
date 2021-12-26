from django.db import models

class Question(models.Model):
    question_title = models.CharField(max_length=80, default='Опрос', blank = False, null = False, verbose_name='Наименованеие опроса')
    question_text = models.CharField(max_length=200, default='',  blank = True, null=False, verbose_name = '1:')
    question_text2 = models.CharField(max_length=200, default='',  blank = True, null = False, verbose_name='2:')
    question_text3 = models.CharField(max_length=200, default='',  blank = True, null = False, verbose_name='3:')
    question_text4 = models.CharField(max_length=200, default='',  blank = True, null = False, verbose_name='4:')
    votes = models.IntegerField(default=0, verbose_name='Проголосовавших:')

    def __str__(self):
        return self.question_title

    class Meta: 
        verbose_name_plural = 'Опросы'
        verbose_name = 'Опрос'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=400, default='',  blank = True, null = False)
    choice_text2 = models.CharField(max_length=400, default='',  blank = True, null = False)
    choice_text3 = models.CharField(max_length=400, default='',  blank = True, null = False)
    choice_text4 = models.CharField(max_length=400, default='',  blank = True, null = False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'
