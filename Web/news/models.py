from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    intro = models.CharField('Intro', max_length=250)
    full_text = models.TextField('Stat')
    date = models.DateTimeField('Data of publication')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'







