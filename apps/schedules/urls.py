from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.list_schedules, name='list_schedules'),
    path('adicionar/', views.add_schedule, name='add_schedule'),
    path('editar/<int:id_schedule>/', views.edit_schedule, name='edit_schedule'),
    path('excluir/<int:id_schedule>/', views.delete_schedule, name='delete_schedule'),
]