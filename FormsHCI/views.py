from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Domanda
from .forms import SUSForm
import csv


def index(request):
    context = {}
    return HttpResponse("this is index", context)


def create(request):
    context = {}
    return render(request, "create.html", context)


def form(request):

    if request.method == 'POST':
        form = SUSForm(request.POST)

        if form.is_valid():
            form.cleaned_data #i cleaned data vanno messi nel csv
            return HttpResponseRedirect('completed.html') #pagina di form completato

    else:
        form = SUSForm()
    return render(request, "form.html", {'form': form})


# prende i dati da file csv come si fa?
def results(request, form_id):
    context = {}
    #response = HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return render(request, "results.html", context)


def completed(request):
    context = {}
    return render(request, "completed.html", context)