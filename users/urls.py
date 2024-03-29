from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
        path('users/', views.sign_up, name='sign-up-page'),
        path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login_page'),
]
