from django.urls import path
from . import views, homme_views

urlpatterns = [

    # pages pour antiquite
    path('', views.index), # path('indexantiquite/', views.index) ?
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('dateAjoute/<int:id>/', views.dateAjoute), # n° Id est dans url
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),


    path('frise/', views.frise),
    path('saisie/', views.saisie),


    path('ajout/', views.ajout),

    # pages pour homme

    path('ajouthomme/',homme_views.ajout),
    path('traitementhomme/',homme_views.traitement),
    path('updatehomme/<int:id>/',homme_views.update),
    path('updatetraitementhomme/<int:id>/',homme_views.updatetraitement),
    path('deletehomme/<int:id>/',homme_views.delete),

]
