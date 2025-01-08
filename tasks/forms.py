from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...', 'class': 'form-control'}))

	class Meta:
		model = Task
		fields = '__all__'
