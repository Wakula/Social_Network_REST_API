from django.db import models
from django.db.models import Count


class LikeManager(models.Manager):
    def get_analytics(self, user_profile, date_from, date_to):
        queryset = self.filter(user_profile=user_profile)
        if date_from and date_to:
            queryset = queryset.filter(date_liked__range=[date_from, date_to])
        elif date_from:
            queryset = queryset.filter(date_liked__gte=date_from)
        elif date_to:
            queryset = queryset.filter(date_liked_lte=date_to)
        queryset = queryset.values('date_liked')\
            .annotate(likes_amount=Count('id'))\
            .order_by('date_liked')
        return queryset
