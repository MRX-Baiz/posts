from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
        path('sign_up/', views.sign_up, name='sign-up-page'),
        path('profile/', views.profile, name='profile-page'),
        path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='login_page'),
        path('logout/', views.logout_user, name='logout_page'),
        path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
        path('password_reset_sent/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
        path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
