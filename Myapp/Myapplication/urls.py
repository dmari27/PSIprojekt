from django.urls import path
from . import views

urlpatterns = [
    path('typ_wniosku', views.ListaRodzajWniosku.as_view(), name=views.ListaRodzajWniosku.name),
    path('typ_wniosku/<int:pk>', views.WniosekSzczegoly.as_view(), name=views.WniosekSzczegoly.name),
    path('wniosek', views.ListaWnioskow.as_view(), name=views.ListaWnioskow.name),
    path('wniosek/<int:pk>',views.WniosekSzczegoly.as_view(),name=views.WniosekSzczegoly.name),
    path('klienci',views.ListaKlientow.as_view(),name = views.ListaKlientow.name),
    path('klienci/int:pk>',views.KlientSzczegoly.as_view(),name=views.KlientSzczegoly.name),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),




]
