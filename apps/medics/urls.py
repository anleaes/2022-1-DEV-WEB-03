from django.urls import path
from . import views

app_name = 'medics'

urlpatterns = [
    path('', views.list_medics, name='list_medics'),
    path('adicionar/', views.add_medic, name='add_medic'),
    path('editar/<int:id_medic>', views.edit_medic, name='edit_medic'),
    path('excluir/<int:id_medic>', views.delete_medic, name='delete_medic'),
]