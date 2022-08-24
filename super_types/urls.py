from django.urls import path
from . import views

urlpatterns = [
    path('', views.type_list),
    path('<int:pk>/', views.type_by_id)
]