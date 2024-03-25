from django.urls import path
from django.contrib.auth import views as auth_views

from userauths import views

app_name = 'userauths'

urlpatterns = [

        # User Profile
        path('profile/update/', views.profileUpdate, name="profile-update"),

        # User Authentication
        path('sign-up/', views.register, name="sign-up"),
        path('sign-in/', auth_views.LoginView.as_view(template_name="userauths/sign-in.html", redirect_authenticated_user=True), name='sign-in'),
        path('sign-out/', auth_views.LogoutView.as_view(template_name="userauths/sign-out.html"), name='sign-out'), 
]
