from django_filters import rest_framework as filters

from reviews.models import Title


class TitleFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category__slug")
    genre = filters.CharFilter(field_name="genre__slug")
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    year = filters.NumberFilter

    class Meta:
        fields = ('category', 'genre', 'name', 'year',)
        model = Title