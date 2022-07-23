from datetime import timedelta
from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.

class CRUD(models.Model):
    # I didn't know if they were going to understand it in English so I did it in Spanish :D
    idUser = models.CharField(max_length=50, null=False)
    
    
    citizenship_card = "CC"
    identity_card = "TI"
    foreign_ID = "CE" 
    TYPE_OF_ID_USER = (
        (citizenship_card, "Cedula de ciudadania"),
        (identity_card, "Targeta de identidad"),
        (foreign_ID, "Cedula de Extranjeria")
    )

    typeIdUser = models.CharField(
        max_length=2,
        choices=TYPE_OF_ID_USER,
        default=citizenship_card,
    )


    namesUser = models.CharField(max_length=50, null=False)
    surnamesUser = models.CharField(max_length=50, null=False)
    phoneNumberUser = models.CharField(max_length=50, null=True)
    landline = models.CharField(max_length=50, null=True)
    emailUser = models.CharField(max_length=50, null=False)
    titlePQR = models.CharField(max_length=50, null=False)
    typeTiket = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    statusTiket = models.BooleanField(null=False)
    dateofCreate = models.DateTimeField('date published', null=False)

    def time_antique(self):
        return timezone.now() >= self.dateofCreate >= timezone.now() - timedelta(days=1)