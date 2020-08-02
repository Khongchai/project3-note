from django.shortcuts import render
import datetime

def index(request):
    newyear = datetime.datetime.now()
    return render(request, "newyear/isitnewyear.html", {
        "newyear": newyear.date == 1 and newyear.month == 1
    })
