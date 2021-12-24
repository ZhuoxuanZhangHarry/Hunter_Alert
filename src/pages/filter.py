import django_filters
from .models import Post

class PostFilters(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['yourname', 'description', 'requirement', 'date_posted']