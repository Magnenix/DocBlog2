from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, "blog/index.html", context={"date": datetime.today()})


