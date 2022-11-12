from django.db import models

# Create your models here.
from django.db.models import Model


class Event(Model):
    TYPE_CONCERTS = 'Koncerty'
    TYPE_CINEMA = 'Kina'
    TYPE_SPORT = 'Sport'
    TYPE_THEATERS = 'Divadla'
    TYPE_EXPOSITION = 'Výstavy'
    TYPE_EXHIBITION = 'Vernisáže'
    TYPE_FAIR= 'Veletrhy'
    TYPE_ENTERTAINMENT= 'Zábavy'
    TYPE_BALL= 'Bály'

    TYPE_CHOICES =[
         # (DB_CODE, "human_readable_name")
        (TYPE_BALL, 'Bály a taneční akce'),
        (TYPE_THEATERS, 'Divadelní představení'),
        (TYPE_CINEMA, 'Kina'),
        (TYPE_CONCERTS, 'Koncerty'),
        (TYPE_SPORT,'Sportovní akce'),
        (TYPE_FAIR, 'Veletrhy'),
        (TYPE_EXHIBITION, 'Vernisáže'),
        (TYPE_EXPOSITION, 'Výstavy'),
        (TYPE_ENTERTAINMENT, 'Zábavy')

    ]


    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=200, default=TYPE_CONCERTS)
    city = models.CharField(max_length=200) #lze dodělat jako model
    performer = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ticket_seat_nr = models.IntegerField(default=0)
    #ticket_reserved_nr = models.IntegerField(default=0)
    ticket_stand_nr = models.IntegerField(default=20)
    price = models.FloatField(default=100)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date', 'performer', 'city', '-updated' ]