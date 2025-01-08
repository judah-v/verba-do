from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.shortcuts import redirect
from .processing import update_tasklist
import json
class Home(LoginRequiredMixin, CreateView, ListView):
	model = Task
	template_name = 'tasks/list.html'
	context_object_name = 'tasks'
	form_class = TaskForm
	success_url = '/'

	def get_context_data(self, **kwargs):
		self.object_list = self.request.user.task_set.all()
		context = super().get_context_data(**kwargs)
		return context

class UpdateTask(UpdateView):
	template_name = 'tasks/update_task.html'
	model = Task
	success_url = '/'
	fields = '__all__'

class RegistrationSuccessView(TemplateView):
	template_name = 'registration/success.html'

def delete_task(request, pk):
	Task.objects.get(pk=pk).delete()
	return redirect('home')
	

def execute_command(request):
	update_tasklist(request)
	return redirect('home')

def create_user(request):
	data = json.loads(request.body.decode())
	name = data['name'].replace('"', '')
	password = data['password'].replace('"', '')
	# print(f"\n\n\n{name}\n{password}\n\n")
	user = User.objects.create_user(username=name, password=password)
	user.save()
	request.user = user
	return redirect('registration_success')
