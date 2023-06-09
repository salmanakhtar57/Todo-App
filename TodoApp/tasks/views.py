from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    
def index(request):
    tasks = request.session.get("tasks", [])
    return render(request, "tasks/index.html", {"tasks": tasks})

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks = request.session.get("tasks", [])
            tasks.append(task)
            request.session["tasks"] = tasks
            return HttpResponseRedirect(reverse("tasks:index"))
    else:
        form = NewTaskForm()

    return render(request, "tasks/add.html", {"form": form})

