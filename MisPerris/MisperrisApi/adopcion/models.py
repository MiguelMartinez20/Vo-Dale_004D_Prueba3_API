from django.db import models

# Create your models here.

class Dog(models.Model):

    RESCATADO = 'Rescatado'
    DISPONIBLE = 'Disponible'
    ADOPTADO = 'Adoptado'

    STATE_CHOICES = (
        (RESCATADO, 'Rescatado'),
        (DISPONIBLE, 'Disponible'),
        (ADOPTADO, 'Adoptado'),
    )

    name = models.CharField(max_length=30)
    race = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=RESCATADO)