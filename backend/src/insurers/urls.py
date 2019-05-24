from django.urls import path

from . import views

urlpatterns = [
    path('', views.InusrerListView.as_view()),
]
