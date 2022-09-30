from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    creator = filters.ModelMultipleChoiceFilter(to_field_name = 'creator_id', queryset = Advertisement.objects.all())
    created_at = filters.DateFromToRangeFilter()
    status = filters.CharFilter(field_name = 'status')

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status']