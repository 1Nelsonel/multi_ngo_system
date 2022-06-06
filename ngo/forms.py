from django.forms import ModelForm
from .models import User, Project, Evente
from django.contrib.auth.forms import UserCreationForm
# from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['user']

class EventForm(ModelForm):
    class Meta:
        model = Evente
        fields = '__all__'
        exclude = ['user']

        
    
        