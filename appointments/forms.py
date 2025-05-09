from django import forms
from .models import Scheduling

DISEASE_CHOICES = [
    ('gripe', 'Gripe'),
    ('dengue', 'Dengue'),
    ('covid', 'COVID-19'),
    ('zika', 'Zika Vírus'),
    ('chikungunya', 'Chikungunya'),
    ('hepatite', 'Hepatite'),
    ('outro', 'Outro'),
]

class SchedulingForm(forms.ModelForm):
    class Meta:
        model = Scheduling
        fields = ['name', 'cpf', 'date', 'specialty', 'time', 'observations']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'specialty': forms.Select(choices=DISEASE_CHOICES, attrs={'class': 'form-select'}),
            'observations': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if not date or not time:
            raise forms.ValidationError("Por favor, preencha todos os campos obrigatórios.")

        if Scheduling.objects.filter(date=date, time=time).exists():
            raise forms.ValidationError("Já existe um agendamento para esse horário.")

        return cleaned_data
