from django.shortcuts import render
from .forms import EventForm
from django.http import HttpResponseRedirect
from .models import EventUser


def home(request):
    users_count = EventUser.objects.count()

    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("?submitted")
    else:
        form = EventForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request,
        "eventapp/home.html",
        {"form": form, "submitted": submitted, "users_count": users_count},
    )


def about(request):
    return render(request, "eventapp/about.html", {})
