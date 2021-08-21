from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("signup/", views.sign_Up , name="signup"),
    path("login/", views.loginPage , name="login"),
    path("logout/", views.logoutPage , name="logout"),
]
