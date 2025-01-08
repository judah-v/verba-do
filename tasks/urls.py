from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.Home.as_view(), name="home"),
	path('command', views.execute_command, name="command"),
	path('update_task/<str:pk>/', views.UpdateTask.as_view(), name="update_task"),
	path('delete/<str:pk>/', views.delete_task, name="delete"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/success/', views.RegistrationSuccessView.as_view(), name="registration_success"),
	path('new/', views.create_user, name="createuser"),
    
    
    
]