from django.shortcuts import render, redirect

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
    return redirect(f"/todo/?pk={todo.pk}")


def detail_view(request):
    pk = request.GET.get('pk')
    todo = ToDo.objects.get(pk=pk)
    print(todo.description)
    return render(request, 'todo.html', context={'todo': todo})
