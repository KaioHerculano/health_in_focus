from django.shortcuts import render, redirect
from .forms import SchedulingForm

def schedule_appointment(request):
    if request.method == 'POST':
        form = SchedulingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = SchedulingForm()
    return render(request, 'schedule_appointment.html', {'form': form})

def no_functionality(request):
    return render(request, 'no_functionality.html')

def patient_rights(request):
    return render(request, 'rights.html')

def home(request):
    return render(request, 'home.html')
