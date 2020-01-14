from rest_framework import serializers
from .models import SHell

'''
Serializers in Django REST api
serializers allows to convert the django data models into desired format like text-based
Django models and query sets can not be convertible into json format so that we convert them into python native type such
as lists and dictionaries and then the conversion to  the json format django serializers will do the specific things for us
serializers also help us  in storing the data into django models and query sets. The incoming format of data will 
not compatible with django built in types so that serializers make the conversion easier also.
'''


class SHell_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SHell
        fields = '__all__'
