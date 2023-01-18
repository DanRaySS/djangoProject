from django.urls import path

from .views import DemandPage, GeographyPage, HomePage, LastVacancyPage, SkillsPage


urlpatterns = [
    path('', HomePage, name='homePage'),
    path('DemandPage/', DemandPage, name='demandPage'),
    path('GeographyPage/', GeographyPage, name='geographyPage'),
    path('SkillsPage/', SkillsPage, name='skillsPage'),
    path('LastVacancyPage/', LastVacancyPage, name='lastVacancyPage'),
]