from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Tasks

class TaskListView(ListView):
    model=Tasks
    template_name='task_list.html'

class TaskCreateView(CreateView):
    model=Tasks
    template_name='task_new.html'
    fields= ('body' ,)

class TaskDeleteView(DeleteView):
    model= Tasks
    template_name='task_delete.html'
    success_url=reverse_lazy('task_list')
class TaskUpdateView(UpdateView):
    model=Tasks
    fields=('body',)
    template_name='task_edit.html'

