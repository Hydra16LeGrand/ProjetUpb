from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from . import views

import random



urlpatterns = [
    path('Probleme/Poser-un-probleme/', views.Probleme.PoserProbleme.as_view(), name='poser_probleme'),
    path('Probleme/liste-des-problemes/', views.Probleme.ListerProbleme.as_view(), name='lister_probleme'),
    path('', views.Probleme.ListerProbleme.as_view(), name='lister_probleme'),
    path('Probleme/rechercher-probleme/', views.Probleme.RechercherProbleme.as_view(), name='rechercher_probleme'),
    path('Probleme/detail-probleme/<int:pk>/', views.Probleme.DetailProbleme.as_view(), name='detail_probleme'),

    path('Dashboard/modifier-probleme/?<int:pk>/', views.Dashboard.ModifierProbleme.as_view(), name='modifier_probleme'),
    path('Dashboard/mes-problemes/', views.Dashboard.MesProblemes.as_view(), name='mes_problemes'),
    path('Dashboard/mes-reponses/', views.Dashboard.MesReponses.as_view(), name='mes_reponses'),

    path('Reponse/donner-reponse/?<int:id_probleme>/', views.Reponse.DonnerReponse.as_view(), name='donner_reponse'),
    path(
    	f'Reponse/solution-probleme/{random.randrange(1, 200)}<int:id_probleme>{random.randrange(1, 200)}/{random.randrange(1, 200)}<int:id_reponse>{random.randrange(1, 200)}', 
    	views.Reponse.SolutionAuProbleme.as_view(), 
    	name='solution_au_probleme'
    	),

    path(f'Reponse/liker-reponse/{random.randrange(1, 200)}<int:id_probleme>{random.randrange(1, 200)}/{random.randrange(1, 200)}<int:id_reponse>{random.randrange(1, 200)}/', 
    	views.Reponse.LikerReponse.as_view(), name='liker_reponse'),
]