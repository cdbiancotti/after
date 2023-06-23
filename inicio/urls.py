from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('gatos/crear/', views.crear_gato, name='crear_gato'),
]
