from django.urls import path

from .views import HomePageView, AboutPageView, PostPageView, HomePageShowPosts

urlpatterns = [
    path('', HomePageShowPosts, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/', PostPageView, name='post'),
]
