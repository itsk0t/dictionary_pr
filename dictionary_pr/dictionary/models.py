from django.db import models


class Word(models.Model):
    name = models.CharField('Название слова', max_length=64)
    text = models.TextField('Определение слова')
    photo = models.ImageField('Изображение', upload_to='images/')

    class Meta:
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/dictionary/{self.id}'

