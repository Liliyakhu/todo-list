from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


# Task views
class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


# Tag views
class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


def toggle_assign_to_done(request, pk):
    task = Task.objects.get(id=pk)
    print(task.done)
    if task.done:  # probably could check if car exists
        task.done = False
        task.save()
    else:
        task.done = True
        task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))
