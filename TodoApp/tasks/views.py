from django.shortcuts import render

tasks = ["Python", "Django", "Flask"]

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })