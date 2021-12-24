from django.urls import path

from .views import HomePageView, AboutPageView, PostPageView, HomePageShowPosts, LogoutView

urlpatterns = [
    path('', HomePageShowPosts, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/', PostPageView, name='post'),
    path('logout/', LogoutView.as_view(), name = 'logout' ),
]
