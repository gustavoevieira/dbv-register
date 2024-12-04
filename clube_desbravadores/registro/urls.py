from django.urls import path
from .views import registro_view, registro_sucesso_view

urlpatterns = [
    path('registrar/', registro_view, name='registro'),
    path('sucesso/', registro_sucesso_view, name='registro_sucesso'),
]
