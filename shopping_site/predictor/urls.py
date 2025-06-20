from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_view, name='predict'),
    path('project-info/', views.project_info, name='project_info'),
]
