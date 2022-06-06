from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ngoDashboard/', views.ngoDashboard, name='ngoDashboard'),
    path('createProject/', views.createProject, name='createProject'),
    path('allprojects/', views.viewProjects, name='allprojects'),
    path('updateproject/<str:pk>/', views.updateProject, name='updateproject'),
    path('delete/<str:pk>/', views.deleteProject, name='delete'),
    path('createEvent/', views.createEvent, name='createEvent'),
    path('events/', views.viewEvents, name='events'),
    path('updateEvent/<str:pk>/', views.updateEvent, name='updateEvent'),   
]