from django.db import models


class Participants(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Location(models.Model):
    name = models.CharField(max_length=255, verbose_name='Meetup location city')
    address = models.CharField(max_length=255, verbose_name='Meetup address')

    def __str__(self):
        return f'{self.name} ({self.address})'


class Meetup(models.Model):
    title = models.CharField(max_length=255, verbose_name='Meetup title')
    slug = models.SlugField(unique=True, verbose_name='Meetup slug')
    organizer_email = models.EmailField(verbose_name='Organizer field')
    description = models.TextField(verbose_name='Meetup description')
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participants, blank=True)

    def __str__(self):
        return self.title
