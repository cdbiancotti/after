from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('gatos/crear/', views.crear_gato, name='crear_gato'),
    path('gatos/', views.listar_gatos, name='gatos'),
    path('gatos/<int:pk>/', views.DetalleGato.as_view(), name='detalle_gato'),
    path('gatos/<int:pk>/modificar/', views.ModificarGato.as_view(), name='modificar_gato'),
    path('gatos/<int:pk>/eliminar/', views.EliminarGato.as_view(), name='eliminar_gato'),
]
