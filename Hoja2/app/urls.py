from django.urls import path
from .views import home, preguntas

urlpatterns = [
    path('', home, name='home'),
    path('preguntas/', preguntas, name='preguntas'),
]