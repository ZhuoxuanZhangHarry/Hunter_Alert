from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'yourname',
            'title',
            'description',
            'dept_name',
            'requirement',
            'deadline',
            'date_posted',
            'email'
        ]
