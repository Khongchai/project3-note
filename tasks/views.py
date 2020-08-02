from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

#before using session = python manage.py migrate to start using database

class NewTaskForms(forms.Form):
    #this task is what gets called in the form.cleaned_data["task"]
    task = forms.CharField(label="New Task", max_length=10, min_length=1)

def index(request):
    #if the current session does not have "tasks" as one of the keys, the create one 
    #with an empty list
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

#the thing inside request.session["some key"] is available globally
def add(request):
    if request.method == "POST":
        #request.POST contains all the data that the user submitted
        form = NewTaskForms(request.POST)
        if form.is_valid():

            #form.cleaned_data returns a dictionary of all submitted data
             task = form.cleaned_data["task"]
             #append the list of key "tasks" in side the session with whatever is stored in the task variable
             request.session["tasks"] += [task]
             #go back to this page
             return HttpResponseRedirect(reverse("tasks:index"))
        else:
            #if task is not valid, rerender the form with all the info from request.POST, which 
            #will have been saved into the form variable up there.
            return render(request, "tasks/add.html", {
                "form": form
            })
    #this return refreshes the page after user clicks on submit
    #and also if method is GET
    return render(request, "tasks/add.html", {
        "form": NewTaskForms()
    })
