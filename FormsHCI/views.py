from django.shortcuts import render
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Quesito, FormEncoder
from .models import Form
import csv
import json


def index(request):
    context = {}
    return HttpResponse("this is index", context)
    #return JsonResponse({'comments' : comments}) restituisce un json, serve un dizionario


def create(request):
    context = {}
    return render(request, "create.html", context)


def salvaForm(request):

    form = Form(request.POST)


def form(request):

    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            form.cleaned_data #i cleaned data vanno messi nel csv
            return HttpResponseRedirect('completed.html') #pagina di form completato

    else:
        form = Form()
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


form_data = serializers.serialize("json", Form.objects.all(), cls=FormEncoder)