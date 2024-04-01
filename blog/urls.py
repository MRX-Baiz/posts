from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('post_details/<int:pk>/', views.post_details, name='details-page'),
    path('post_edit/<int:pk>/', views.post_edit, name='edit-page'),
    path('post_delete/<int:pk>/', views.post_delete, name='delete-page'),
]
