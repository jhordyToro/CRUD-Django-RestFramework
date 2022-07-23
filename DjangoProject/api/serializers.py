from pyexpat import model
from rest_framework import serializers
from .models import CRUD

class CRUDserializer(serializers.ModelSerializer):
    class Meta:
        model = CRUD
        fields = '__all__'