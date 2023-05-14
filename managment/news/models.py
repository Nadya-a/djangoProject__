from django.db import models


class Articles(models.Model):
    title = models.CharField('Nazvanie', max_length=100)
    anons = models.CharField('Anons', max_length=150)
    full_text = models.TextField('Full text')
    date = models.DateTimeField('Date: ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


