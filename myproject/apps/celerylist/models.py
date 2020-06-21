import datetime
from django.db import models
from django.utils import timezone


class Celery(models.Model):
    celery_title = models.CharField('Заголовок письма', max_length= 200)
    celery_text = models.TextField('Описание')
    pub_date = models.DateTimeField('Дата пубдикации')

    def __str__(self):
        return self.celery_title

    def was_publ_rec(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Служебное письмо'
        verbose_name_plural = 'Служебные письма'

class list(models.Model):
    article = models.ForeignKey(Celery, on_delete = models.CASCADE)
    spes_name = models.CharField('Исполнитель', max_length= 200)
    comment_text = models.CharField('Текст коментария', max_length=200)

    def __str__(self):
        return self.spes_name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'