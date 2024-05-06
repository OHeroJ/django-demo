from django.shortcuts import render
from .models import Task
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .mixins import SprintTaskWithinRangeMixin

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'
    
class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

class TaskCreateView(SprintTaskWithinRangeMixin, CreateView):
    model = Task
    template_name = 'task_create.html'
    fields = ('name', 'description', 'start_date', 'end_date',)
    def get_success_url(self) -> str:
        return reverse_lazy('tasks:task-detail', kwargs={'pk': self.object.id})

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    fields = ('name', 'description', 'start_date', 'end_date',)
    def get_success_url(self) -> str:
        return reverse_lazy('tasks:task-detail', kwargs={'pk': self.object.id})
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasks:task-list')