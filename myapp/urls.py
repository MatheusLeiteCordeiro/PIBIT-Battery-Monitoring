from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('Baterry_Dashboards/', views.Battery_Dashboards, name='Baterry_Dashboards'),
    path(r'^app/(?P<id>\d+)/new-page/$', views.tabela, name='tabela'),
    path('mvp/', views.mvp, name='mvp'),
    path('monitoramento_baterias/', views.monitoramento_baterias, name='monitoramento_baterias'),
    path('monitoramento_trafos/', views.monitoramento_trafos, name='monitoramento_trafos')

]
