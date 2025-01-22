from rest_framework import serializers
from .models import register,Login

class registerserializers(serializers.ModelSerializer):
 class Meta:
    model=register
    fields="__all__" 

class loginserializers(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields='__all__'