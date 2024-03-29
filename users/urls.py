from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
        path('sign_up/', views.sign_up, name='sign-up-page'),
        path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='login_page'),
        path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout_page'),
]
