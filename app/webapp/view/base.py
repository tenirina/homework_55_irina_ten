from django.shortcuts import render

from webapp.models import ToDo


def index_view(request):
    to_does = ToDo.objects.exclude(is_delete=True)
    for el in to_does:
        el.status = el.get_status_display()
    context = {
        "to_does": to_does
    }
    return render(request, "index.html", context)
