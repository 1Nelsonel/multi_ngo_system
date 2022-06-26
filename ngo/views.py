from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Evente, Project, User
from .forms import ProjectForm, EventForm
import datetime

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'ngo/home.html', context)
 
def ngoDashboard(request):
    projects = Project.objects.all()
    allevents = Evente.objects.all()
    context = {'projects': projects, 'allevents': allevents}
    return render(request, 'ngo/ngo-dashboard.html', context)

def createProject(request):
    form = ProjectForm(request.POST, request.FILES)
    if request.method == 'POST':              
        Project.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            image =request.FILES['image'],
        ) 
        messages.success(request, 'Room created')
        return redirect('ngoDashboard')

    context = {'form': form, }
    return render(request, 'ngo/create-project.html', context)

@login_required(login_url='accounts/login')
def viewProjects(request):
    allprojects = Project.objects.all()
    context = {'allprojects': allprojects}
    return render(request, 'ngo/projects.html', context)

@login_required(login_url='/accounts/login/')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)

    form = ProjectForm(instance=project)
    
    if request.user != project.user:
        messages.warning(request, 'Invalid request!! ')
        return redirect('ngoDashboard')

    if request.method == 'POST':
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        
        if len(request.FILES) != 0:
            project.image =request.FILES['image']

        project.save()
        messages.success(request, 'Project updated')
        return redirect('allprojects')
    context = {'form': form, 'project': project }
    return render(request, 'ngo/update-project.html', context)

@login_required(login_url='accounts/login')
def deleteProject(request, pk):
    projectone = Project.objects.get(id=pk)

    if request.user != projectone.user:
        messages.warning(request, 'Invalid request!! ')
        return redirect('ngoDashboard')

    if request.method == 'POST':
        projectone.delete()
        messages.warning(request, 'Project deleted')
        return redirect('ngoDashboard')
    context = {'obj': projectone}
    return render(request, 'ngo/delete-project.html', context)

@login_required(login_url='accounts/login')
def createEvent(request):
    if request.method == 'POST':
        event = Evente()
        event.user = request.user
        event.name = request.POST.get('name')   
        event.eventdate = request.POST.get('eventdate')
        event.description = request.POST.get('description')

        if len(request.FILES) != 0:
            event.image =request.FILES['image']

        event.save()             
        messages.success(request, 'Event created')
        return redirect('events')
    return render(request, 'ngo/create-event.html')

@login_required(login_url='accounts/login')
def viewEvents(request):
    allevents = Evente.objects.all()
    context = {'allevents': allevents}
    return render(request, 'ngo/events.html', context)

def updateEvent(request, pk):
    event = Evente.objects.get(id=pk)
    
    form = EventForm(instance=event)

    if request.user != event.user:
        messages.warning(request, 'Invalid request!! ')
        return redirect('ngoDashboard')

    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.eventdate = request.POST.get('eventdate')
        event.description = request.POST.get('description')
        
        if len(request.FILES) != 0:
            event.image =request.FILES['image']

        event.save()
        messages.success(request, 'Room updated')
        return redirect('events')
    context = {'event': event, 'form': form,  }
    return render(request, 'ngo/update-event.html', context)

@login_required(login_url='accounts/login')
def deleteProject(request, pk):
    evente = Evente.objects.get(id=pk)

    if request.user != evente.user:
        messages.warning(request, 'Invalid request!! ')
        return redirect('ngoDashboard')

    if request.method == 'POST':
        evente.delete()
        messages.warning(request, 'Event deleted')
        return redirect('ngoDashboard')
    context = {'obj': evente}
    return render(request, 'ngo/delete-project.html', context)



