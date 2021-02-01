from rest_framework import serializers
from .models import RodzajWniosku,Wniosek,Klient,Administrator
from django.contrib.auth.models import User

class RodzajWnioskuSerializer(serializers.ModelSerializer):

    wnioski = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='typ_wniosku')
    class Meta:
        model = RodzajWniosku
        fields = '__all__'

class WniosekSerializer(serializers.ModelSerializer):
    typ_wniosku = serializers.SlugRelatedField(queryset=RodzajWniosku.objects.all(), slug_field='typ')
    class Meta:
        model = Wniosek
        fields = '__all__'

class KlientSerializer(serializers.ModelSerializer):
    skladajacy  =  serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='wnioskodawca')

    class Meta:
        model = Klient
        fields = '__all'

class UserWniosekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wniosek
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    wnioski = UserWniosekSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['url','pk','username','books']

