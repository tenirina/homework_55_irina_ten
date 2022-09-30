from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import ToDo


def add_view(request):
    if request.method == "GET":
        choices = ToDo.CHOICES
        return render(request, 'add.html', context={'choices': choices})
    todo_data = {
        'text': request.POST.get('text'),
        'status': request.POST.get('select'),
        'completion_data': request.POST.get('completion_data'),
        'description': request.POST.get('textarea')
    }
    todo = ToDo.objects.create(**todo_data)
    return redirect(reverse('todo', kwargs={'pk': todo.pk}))


def detail_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    status = todo.get_status_display()
    todo.status = status
    return render(request, 'todo.html', context={'todo': todo})


def edit_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        todo.text = request.POST.get("text")
        todo.status = request.POST.get("select")
        todo.description = request.POST.get("textarea")
        todo.completion_data = request.POST.get("completion_data")
        todo.save()
        return redirect('todo', pk=todo.pk)
    return render(request, 'edit.html', context={'todo': todo, 'choices': ToDo.CHOICES})


def delete_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, "confirm_delete.html", context={'todo': todo})


def confirm_delete_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return redirect("index")

