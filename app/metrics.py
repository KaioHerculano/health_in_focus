from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from appointments import models


def get_disease_metrics():
    try:
        thirty_days_ago = timezone.now() - timedelta(days=30)
        
        recent_appointments = models.Scheduling.objects.filter(
            date__gte=thirty_days_ago
        )
        
        specialty_counts = recent_appointments.values('specialty').annotate(
            total=Count('id')
        ).order_by('-total')
        
        labels = [item['specialty'] for item in specialty_counts]
        counts = [item['total'] for item in specialty_counts]
        
        return labels, counts
        
    except Exception as e:
        print(f"Erro em get_disease_metrics: {str(e)}")
        return [], []