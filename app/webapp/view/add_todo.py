from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import ToDoForm
from webapp.models import ToDo


def add_view(request):
    form = ToDoForm()
    if request.method == "GET":
        choices = ToDo.CHOICES
        return render(request, 'add.html', context={'choices': choices, 'form': form})
    form = ToDoForm(request.POST)
    if not form.is_valid():
        return render(request, 'add.html', context={'choices': ToDo.CHOICES, 'form': form})
    todo = ToDo.objects.create(**form.cleaned_data)
    return redirect(reverse('todo', kwargs={'pk': todo.pk}))


def detail_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    status = todo.get_status_display()
    todo.status = status
    return render(request, 'todo.html', context={'todo': todo})


def edit_view(request, pk):
    form = ToDoForm()
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo.text = form.cleaned_data["text"]
            todo.status = form.cleaned_data["status"]
            todo.description = form.cleaned_data["description"]
            todo.completion_data = form.cleaned_data["completion_data"]
            todo.save()
            return redirect('todo', pk=todo.pk)
    return render(request, 'edit.html', context={'todo': todo, 'choices': ToDo.CHOICES, 'form': form})


def delete_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, "confirm_delete.html", context={'todo': todo})


def confirm_delete_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect("index")

