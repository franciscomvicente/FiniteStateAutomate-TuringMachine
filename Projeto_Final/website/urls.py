from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "website"

urlpatterns = [
    path('', views.introducao, name='introducao'),
    path('afd', views.afd, name='afd'),
    path('turing', views.turing, name='turing'),
    path('oafd/', views.option_afd_view, name='option'),
    path('nova/', views.novo_afd_view, name='novo'),
    path('jsonAFD/', views.json_afd_view, name='json'),
    path('editaAFD/<int:afd_id>', views.edita_afd_view, name='edita'),
    path('apagaAFD/<int:afd_id>', views.apaga_afd_view, name='apaga'),
    path('detalhesAFD/<int:afd_id>', views.detalhes_afd_view, name='detalhes'),
    path('sequenciaAFD/<int:afd_id>', views.sequencia_afd_view, name='sequencia'),
    path('otm/', views.option_tm_view, name='optionTM'),
    path('novaTM/', views.novo_tm_view, name='novoTM'),
    path('jsonTM/', views.json_tm_view, name='jsonTM'),
    path('editaTM/<int:tm_id>', views.edita_tm_view, name='editaTM'),
    path('apagaTM/<int:tm_id>', views.apaga_tm_view, name='apagaTM'),
    path('detalhesTM/<int:tm_id>', views.detalhes_tm_view, name='detalhesTM'),
    path('sequenciaTM/<int:tm_id>', views.sequencia_tm_view, name='sequenciaTM'),
]

urlpatterns += staticfiles_urlpatterns()