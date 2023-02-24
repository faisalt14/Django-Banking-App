from django.urls import path

from accounts.views import Register, Login, ProfileView, Logout, EditProfile

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout', Logout.as_view()),
    path('profile/view/', ProfileView.as_view()),
    path('profile/edit/', EditProfile.as_view())
]