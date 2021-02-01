from django.db import models


# Create your models here.
class RodzajWniosku(models.Model):

    typ = models.CharField(max_length=400,unique=True)

    class Meta:
        ordering = ('typ',)
    def __str__(self):
        return self.typ

class Klient(models.Model):
    objects = None
    imie = models.CharField(max_length=300)
    nazwisko = models.CharField(max_length=300)
    PESEL = models.IntegerField(unique = True)
    adres = models.CharField(max_length = 1000)
    data_urodzin = models.DateField()
    class Meta:
         ordering = ('PESEL',)

    def __str__(self):
        return  self.PESEL


class Wniosek(models.Model):
    objects = None
    typ_wniosku = models.ForeignKey(RodzajWniosku,related_name='wnioski',on_delete = models.CASCADE)
    uzasadnienie = models.CharField(max_length=3000)
    Data_zlozenia = models.DateTimeField(auto_now_add= True)
    numer_wniosku = models.IntegerField(unique=True)
    skladajacy = models.ForeignKey(Klient,related_name='wnioski', on_delete= models.CASCADE,default = None)

    class Meta:
        ordering = ('numer_wniosku',)
    def __str__(self):
        return self.typ_wniosku





class Administrator(models.Model):
    imie = models.CharField(max_length=300)
    nazwisko = models.CharField(max_length=300)
    numer_pracownika = models.IntegerField()

    def __str__(self):
        return self.imie



