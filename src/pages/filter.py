import django_filters
from .models import Post

class PostFilters(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['Your_Name', 'Description', 'Date_Posted', 'Email', 'User', 'Deadline']