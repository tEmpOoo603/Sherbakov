from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('reviews/', views.reviews, name='reviews'),
    path('application/', views.submit_application, name='application'),
    path('work-process/', views.work_process, name='work_process'),
]