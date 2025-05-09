# views.py
from django.views.generic import TemplateView
from .metrics import get_disease_metrics

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            labels, counts = get_disease_metrics()
            context['labels'] = labels or ["Sem dados"]
            context['counts'] = counts or [0]
        except Exception as e:
            print(f"Erro ao gerar métricas: {str(e)}")
            context['labels'] = ["Erro"]
            context['counts'] = [0]
            
        return context