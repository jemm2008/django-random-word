from django.urls import path
from . import views
urlpatterns = [
    path('', views.rword),
    path('random_word/', views.rword),
    path('accion/', views.accion)
]
