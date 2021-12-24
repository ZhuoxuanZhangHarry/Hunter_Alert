from django.urls import path

<<<<<<< Updated upstream
from .views import HomePageView, AboutPageView, PostPageView, HomePageShowPosts, LogoutView
=======
from .views import HomePageView, AboutPageView, PostPageView
>>>>>>> Stashed changes

urlpatterns = [
    path('', HomePageView, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/', PostPageView, name='post'),
    path('logout/', LogoutView.as_view(), name = 'logout' ),
]
