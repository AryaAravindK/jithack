
from django.urls import path
from . import views

urlpatterns = [
    path('take-survey/', views.survey, name='survey'),
    
    
]