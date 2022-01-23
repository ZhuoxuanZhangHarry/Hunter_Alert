from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'Your_Name',
            'Title',
            'Description',
            'Department',
            'Requirement',
            'Deadline',
            'Date_Posted',
            'Email'
        ]
