
from django.urls import path
from drinks import views


urlpatterns = [
    path('drinks/', views.drink_list),
    path("drinks/<int:id>", views.drink_details),
]