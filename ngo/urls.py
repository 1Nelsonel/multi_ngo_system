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
    path('projectMain/',views.projectMain, name='projectMain'),
    path('projectMainsingle/<str:pk>/', views.projectMainsingle, name='projectMainsingle'),
    path('eventMain/', views.eventMain, name='eventMain'),
    path('eventMainsingle/<str:pk>/', views.eventMainsingle, name='eventMainsingle'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteerProject/', views.volunteerProject, name='volunteerProject'),
    path('volunteerProjectjoin/<str:pk>/', views.volunteerProjectjoin, name='volunteerProjectjoin'),
]