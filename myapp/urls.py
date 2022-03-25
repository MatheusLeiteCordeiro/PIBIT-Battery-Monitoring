from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'^app/(?P<id>\d+)/new-page/$', views.tabela, name='tabela'),
    path('mvp/', views.mvp, name='mvp'),
    path('sla/', views.home, name='sla'),
    path('monitoramento_baterias/', views.monitoramento_baterias, name='monitoramento_baterias'),
    path('monitoramento_trafos/', views.monitoramento_trafos, name='monitoramento_trafos')

]
