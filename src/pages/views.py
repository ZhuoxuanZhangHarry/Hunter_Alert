from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import PostForm

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

def PostPageView(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "pages/post.html", context)