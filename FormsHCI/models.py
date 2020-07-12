from django.db import models
from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django.core.files import File
import json
import csv


# classe Domanda
class Domanda(models.Model):
    testoDomanda = models.CharField(max_length=200)

    def __init__(self, testoDomanda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.testoDomanda = testoDomanda


# classe Risposta generica
class Risposta(models.Model):
    #tipi
    BREVE = 'breve'
    PARAGRAFO = 'paragrafo'
    CHECKBOX = 'checkbox'
    MULTIPLA = 'multipla'
    ELENCO = 'elenco'
    DATA_ORA = 'dataora'
    UPLOAD = 'upload'

    # lista dei vari tipi di risposta
    listaTipi = [BREVE, PARAGRAFO, CHECKBOX, MULTIPLA, ELENCO, DATA_ORA, UPLOAD]

    def __init__(self, listaTipi, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.listaTipi = listaTipi

    # selezionare il tipo di Risposta
    def scegliTipo(self):
        for tipo in self.listaTipi:
            if tipo == Risposta.BREVE:
                self.risposta = RispostaBreve

            elif tipo == Risposta.PARAGRAFO:
                self.risposta = RispostaParagrafo

            elif tipo == Risposta.CHECKBOX:
                self.risposta = RispostaCheckbox

            elif tipo == Risposta.MULTIPLA:
                self.risposta = RispostaMultipla

            elif tipo == Risposta.ELENCO:
                self.risposta = RispostaElenco

            elif tipo == Risposta.DATA_ORA:
                self.risposta = RispostaDataOra

            elif tipo == Risposta.UPLOAD:
                self.risposta = RispostaUpload
            else:
                Exception('Tipo non valido')

            return tipo


class RispostaBreve(Risposta):
    risposta = forms.CharField(max_length=100, label=Domanda)

    def __init__(self, risposta):
        super(Risposta, self).__init__()
        self.risposta = risposta


class RispostaParagrafo(Risposta):
    risposta = forms.CharField(max_length=500, widget=forms.Textarea, label=Domanda)

    def __init__(self, risposta):
        super(Risposta, self).__init__()
        self.risposta = risposta


class RispostaCheckbox(Risposta):
    OPTIONS = []

    risposta = forms.MultipleChoiceField(choices=OPTIONS, widget=forms.CheckboxSelectMultiple, label=Domanda)

    def __init__(self, risposta, OPTIONS):
        super(Risposta, self).__init__()
        self.risposta = risposta
        self.OPTIONS = OPTIONS

    def add_option(self):
        self.OPTIONS += self.OPTIONS


class RispostaMultipla(Risposta):
    OPTIONS = []

    risposta = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=Domanda)

    def __init__(self, risposta, OPTIONS):
        super(Risposta, self).__init__()
        self.risposta = risposta
        self.OPTIONS = OPTIONS

    def add_option(self):
        self.OPTIONS += self.OPTIONS


class RispostaElenco(Risposta):
    OPTIONS = []

    risposta = forms.ChoiceField(choices=OPTIONS, label=Domanda)

    def __init__(self, risposta, OPTIONS):
        super(Risposta, self).__init__()
        self.risposta = risposta
        self.OPTIONS = OPTIONS

    def add_option(self):
        self.OPTIONS += self.OPTIONS


class RispostaDataOra(Risposta):
    risposta = forms.DateField(widget=forms.DateInput, label=Domanda)

    def __init__(self, risposta):
        super(Risposta, self).__init__()
        self.risposta = risposta


class RispostaUpload(Risposta):
    risposta = forms.FileField(widget=forms.FileInput, label=Domanda)

    def __init__(self, risposta):
        super(Risposta, self).__init__()
        self.risposta = risposta


# classe Quesito: composta da Domanda + Risposta
class Quesito(models.Model):
    testoQuesito = models.ForeignKey(Domanda, on_delete=models.CASCADE)

    # per stabilire il tipo di risposta
    for el in Risposta.listaTipi:
        if el == Risposta.BREVE:
            risposta = models.ForeignKey(RispostaBreve, on_delete=models.CASCADE)

        elif el == Risposta.PARAGRAFO:
            risposta = models.ForeignKey(RispostaParagrafo, on_delete=models.CASCADE)

        elif el == Risposta.CHECKBOX:
            risposta = models.ForeignKey(RispostaCheckbox, on_delete=models.CASCADE)

        elif el == Risposta.MULTIPLA:
            risposta = models.ForeignKey(RispostaMultipla, on_delete=models.CASCADE)

        elif el == Risposta.DATA_ORA:
            risposta = models.ForeignKey(RispostaDataOra, on_delete=models.CASCADE)

        elif el == Risposta.UPLOAD:
            risposta = models.ForeignKey(RispostaUpload, on_delete=models.CASCADE)

        else:
            Exception('Tipo non valido per quesito')

    def __init__(self, testoQuesito, risposta, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.testoQuesito = testoQuesito
        self.risposta = risposta


# classe Form: nome + lista di quesiti
class Form(models.Model):
    nomeForm = models.CharField(max_length=100)
    quesito = models.ForeignKey(Quesito, on_delete=models.CASCADE)

    quesiti = []

    def __str__(self):
        return self.nomeForm

    def __init__(self, nomeForm, quesito, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nomeForm = nomeForm
        self.quesito = quesito

        for quesito in self.quesiti:
            self.quesiti.append(quesito)

    def salvaForm(self):
        with open(self.nomeForm + '.json', 'w') as outfile:
            json.dump(self.nomeForm, outfile)
            json.dump(self.quesiti, outfile, indent=4)


class FormEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, Form):
            return str(obj)
        return super().default(obj)