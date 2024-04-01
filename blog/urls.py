from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('post_details/<int:pk>/', views.post_detail, name='details-page'),
]
