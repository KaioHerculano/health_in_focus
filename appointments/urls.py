from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('appointments/filter/', views.AppointmentCalendarView.as_view(), name='schedule_list'),
    path('schedule/create/', views.CreateAppointmentView.as_view(), name='schedule_create'),
    path('error/functionality/', views.ErrorFunctionalityView.as_view(), name='error_functionality'),
    path('rights/list/', views.ListPatientRightsView.as_view(), name='rights_list'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
