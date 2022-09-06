from django.urls import path
from . import views

app_name = 'Task_app'

urlpatterns = [
    path('',views.TaskView.as_view(),name='home'),
    path('deletar-task/<slug:task_id>',views.deletar_task,name='deletar_task'),
]
