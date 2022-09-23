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
    print(todo_data)
    todo = ToDo.objects.create(**todo_data)
    return redirect(reverse('todo', kwargs={'pk': todo.pk}))


def detail_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    status = todo.get_status_display()
    todo.status = status
    return render(request, 'todo.html', context={'todo': todo})
