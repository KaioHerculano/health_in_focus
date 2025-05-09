from django.views.generic import TemplateView, CreateView, DeleteView
from datetime import datetime
from django.urls import reverse_lazy
from .models import Scheduling
from .forms import SchedulingForm


class AppointmentCalendarView(TemplateView):
    template_name = 'list_appointments.html'

    def post(self, request, *args, **kwargs):
        date_str = request.POST.get('filter_date')
        try:
            selected_date = datetime.strptime(date_str, '%d/%m/%Y').date()
            appointments = Scheduling.objects.filter(date=selected_date)
        except (ValueError, TypeError):
            selected_date = None
            appointments = []

        return self.render_to_response({
            'appointments': appointments,
            'selected_date': selected_date.strftime('%d/%m/%Y') if selected_date else 'Data inválida'
        })

    def get(self, request, *args, **kwargs):
        today = datetime.today().date()
        appointments = Scheduling.objects.filter(date=today)
        return self.render_to_response({
            'appointments': appointments,
            'selected_date': today.strftime('%d/%m/%Y')
        })

class CreateAppointmentView(CreateView):
    template_name = 'create_appointments.html'
    form_class = SchedulingForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteAppointmentView(DeleteView):
    model = Scheduling
    template_name = 'delete_appointment.html'  # Template para confirmação de exclusão
    success_url = reverse_lazy('schedule_list')


class ErrorFunctionalityView(TemplateView):
    template_name = 'error_functionality.html'


class ListPatientRightsView(TemplateView):
    template_name = 'list_rights.html'



class SuccessView(TemplateView):
    template_name = 'success.html'
