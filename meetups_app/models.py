from django.db import models


class Meetup(models.Model):
    title = models.CharField(max_length=255, verbose_name='Meetup title')
    slug = models.SlugField(unique=True, verbose_name='Meetup slug')
    organizer_email = models.EmailField(verbose_name='Organizer field')
    description = models.CharField(max_length=255, verbose_name='Meetup description')
    image = models.ImageField()

    def __str__(self):
        return f'{self.title}'
