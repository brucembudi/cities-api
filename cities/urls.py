from django.urls import path

from .views import ListCity, DetailCity

urlpatterns = [
    path('<int:pk>/', DetailCity.as_view()),
    path('', ListCity.as_view()),
]