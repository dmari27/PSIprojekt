from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import RodzajWniosku,Wniosek,Klient,Administrator
from .serializers import RodzajWnioskuSerializer, UserSerializer, UserWniosekSerializer, Wniosek, Klient, \
    WniosekSerializer, KlientSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet, filters
from rest_framework import permissions
from django.utils import timezone
from django.contrib.auth.models import User


class ListaWnioskow(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wniosek.objects.all()
    serializer_class = WniosekSerializer
    name = 'lista_wnioskow'
    filter_fields = ['typ_wniosku','uzasadnienie','Data_zlozenia','skladajacy','numer_wniosku']
    search_field = ['skladajacy','numer_wniosku']
    ordering_fields = ['Data_zlozenia','typ_wniosku','numer_wniosku']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class WniosekSzczegoly(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wniosek.objects.all()
    serializer_class = WniosekSerializer
    name = 'szczegoly_wniosku'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ListaRodzajWniosku(generics.ListCreateAPIView):
    queryset = RodzajWniosku.objects.all()
    serializer_class = RodzajWnioskuSerializer
    name = 'Lista_Rodzaj_wniosku'
    filterset_fields = ['typ']
    search_fields = ['typ']
    ordering_fields = ['typ']

class ListaRodzajWnioskuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RodzajWniosku.objects.all()
    serializer_class = RodzajWnioskuSerializer
    name = 'Lista_rodzai'


class KlientFilter(FilterSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['nazwisko', 'PESEL']
    ordering = ['nazwisko']
    class Meta:
        model = Klient
        fields = ['nazwisko','PESEL']

class ListaKlientow(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    filter_class = KlientFilter
    ordering = ['nazwisko','PESEL']
    name = 'lista_klientow'

class KlientSzczegoly(generics.RetrieveUpdateDestroyAPIView):
    queryset =Klient.objects.all()
    serializer_class = KlientSerializer
    name = 'Klient_szczegoly'






# class Wniosek_filter(FilterSet):
       # czas = timezone.now()
        #wnioski_zlozone = DateTimeFilter(field_name="Data_zlozenia",lookup_expr='czas')
        #skladajacy = AllValuesFilter(field_name='PESEL')


        #class Meta:
            #model = Wniosek
            #fields = ['Data_zlozenia','PESEL']

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'lista-uzytkownikow'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'lista-uzytkownikow'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):

        return Response({'Wniosek':reverse(ListaWnioskow.name,request=request)})

