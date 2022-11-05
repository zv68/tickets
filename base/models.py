from django.db import models

# Create your models here.
from django.db.models import Model


class Event(Model):
    TYPE_CONCERTS = 'Concerts'
    TYPE_CINEMA = 'Cinema'
    TYPE_SPORT = 'Sport'
    TYPE_THEATERS = 'Theaters'

    TYPE_CHOICES =[
        (TYPE_CONCERTS,'Concerts'), # (DB_CODE, "human_readable_name")
        (TYPE_CINEMA,'Cinema'),
        (TYPE_SPORT,'Sport'),
        (TYPE_THEATERS,'Theaters'),
    ]


    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=200)
    city = models.CharField(max_length=200) #lze dodělat jako model
    performer = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ticket_seat_nr = models.IntegerField(default=0)
    #ticket_reserved_nr = models.IntegerField(default=0)
    ticket_stand_nr = models.IntegerField(default=20)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date', 'performer', 'city', '-updated' ]