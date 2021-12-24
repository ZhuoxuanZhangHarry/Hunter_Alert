from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

def HomePageShowPosts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'pages/home.html', context)


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

@login_required
def PostPageView(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Post published successfully')
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, "pages/post.html", context)


class LogoutView(TemplateView):
    template_name = 'account/logout.html'