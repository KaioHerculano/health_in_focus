from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('no_functionality/', views.no_functionality, name='no_functionality'),
    path('patient_rights/', views.patient_rights, name='patient_rights'),
]
