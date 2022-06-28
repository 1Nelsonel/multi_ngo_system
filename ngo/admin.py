from multiprocessing import Event
from django.contrib import admin
from . models import Project, Evente, Volunteer

# Register your models here.
admin.site.register(Project)
admin.site.register(Evente)
admin.site.register(Volunteer)