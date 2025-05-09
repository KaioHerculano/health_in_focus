from django.urls import path
from . import views


urlpatterns = [
    path('appointments/filter/', views.AppointmentCalendarView.as_view(), name='schedule_list'),
    path('schedule/create/', views.CreateAppointmentView.as_view(), name='schedule_create'),
    path('schedule/<int:pk>/delete/', views.DeleteAppointmentView.as_view(), name='schedule_delete'),
    path('error/functionality/', views.ErrorFunctionalityView.as_view(), name='error_functionality'),
    path('rights/list/', views.ListPatientRightsView.as_view(), name='rights_list'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
