from django.urls import path
from . import views

app_name = 'pacients'

urlpatterns = [
    path('', views.list_pacients, name='list_pacients'),
    path('adicionar/', views.add_pacient, name='add_pacient'),
    path('editar/<int:id_pacient>', views.edit_pacient, name='edit_pacient'),
    path('excluir/<int:id_pacient>', views.delete_pacient, name='delete_pacient'),
]