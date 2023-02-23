from django.urls import path

from accounts.views import Register, Login, ProfileView, Logout

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout', Logout.as_view()),
    path('profile/view/', ProfileView.as_view())
]