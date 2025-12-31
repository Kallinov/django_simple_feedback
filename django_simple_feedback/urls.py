from django.urls import path

from . import views

app_name = "feedback"

urlpatterns = [
    path('', views.ValidationView.as_view(), name='index'),
    path('success/', views.final, name='success'),
]