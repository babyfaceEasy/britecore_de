from django.urls import path, include
from .views import rest_framework_prac
from risk import views

urlpatterns = [
    # path('risk/', views.RiskTypeList.as_view()),
    path('risk/', views.RiskTypeList.as_view()),
    path('risk/<int:pk>/', views.RiskTypeDetail.as_view()),
    path('risk/ping/', rest_framework_prac),
    path('insurers/', include('insurers.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
