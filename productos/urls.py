from django.urls import path
from . import views

urlpatterns = [
    # URLs de vistas normales
    path('', views.listar_productos, name='listar_productos'),
    # path('agregar/', views.agregar_producto, name='agregar_producto'),
    # path('actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    # path('eliminar/', views.eliminar_producto, name='eliminar_producto'),
    # path('buscar/', views.buscar_producto, name='buscar_producto'),

    # URLs de Django REST Framework
    path('api/', views.ProductoViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_listar_productos'),
    path('api/<int:pk>/', views.ProductoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='api_detalle_producto'),
]