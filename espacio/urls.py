from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'misiones-viewset', views.MisionViewSet)

urlpatterns = [
    # Agencias (Vistas Genéricas)
    path('agencias/', views.AgenciaList.as_view()),
    path('agencias/crear/', views.AgenciaCreate.as_view()),
    path('agencias/<int:pk>/', views.AgenciaDetail.as_view()),
    path('agencias/<int:pk>/borrar/', views.AgenciaDelete.as_view()),

    # Buscador Personalizado
    path('buscar/<str:nombre_agencia>/', views.buscar_misiones_por_agencia),

    # ViewSet (Misiones)
    path('', include(router.urls)),
]