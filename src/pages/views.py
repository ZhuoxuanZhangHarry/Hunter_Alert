from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from .filter import PostFilters
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.views.generic import ListView
#from .models import DeptList

def HomePageView(request):
    posts = Post.objects.all()
    myFilter = PostFilters(request.GET, queryset=posts)
    posts = myFilter.qs
    context = {
        'posts' : posts,
        'myFilter' : myFilter
     }

    return render(request, 'pages/home.html', context)


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

@login_required
def PostPageView(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f'Post published successfully')
            return redirect('home')
    
    context = {
        'form': form
    }
    return render(request, "pages/post.html", context)

def DetailView(request, detail_id):
    detail = Post.objects.get(id=detail_id)
    context = {'detail': detail}
    return render(request, 'pages/detail.html', context)


class LogoutView(TemplateView):
    template_name = 'account/logout.html'

'''class DeptnameList(ListView):
    # specify the model for list view
    #model = DeptList

    def get_dept_data(self, **kwargs):
        deptnames = super().get_dept_data(**kwargs)
        # Add in a QuerySet of all the books
        deptnames['names'] = DeptList.objects.all()
        return deptnames'''