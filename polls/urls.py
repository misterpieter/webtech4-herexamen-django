from django.urls import path

from . import views

urlpatterns = [
    # ex: /infractions/
    path('', views.index, name='index'),
    # ex: /infractions/5/
    path('<int:infraction>/', views.detail, name='detail'),
]