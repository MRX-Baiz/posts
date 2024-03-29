from django.urls import path
from . import views

urlpatterns = [
        path('users/', views.sign_up, name='sign-up-page'),
]
