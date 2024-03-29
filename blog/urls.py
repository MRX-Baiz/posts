from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='home-page'),
    path('about/', views.about, name='about-page'),
]
