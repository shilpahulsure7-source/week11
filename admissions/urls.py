from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission_home, name='admissions'),
]