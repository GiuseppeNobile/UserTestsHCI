from django import forms
from . import models
from .models import RispostaSUS
from .models import Domanda
import csv

# form di esempio
"""
class TestForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=('question', 'other'))
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)"""


class SUSForm(forms.ModelForm):

    class Meta:
        model = Domanda
        fields = ('testoDomanda')

    OPTIONS = (('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5'))

    FIELDS = {
        Domanda.testoDomanda: forms.CharField,
        RispostaSUS.scelta: forms.IntegerField
    }

    domanda01 = "I think that I would like to use this system frequently."
    risposta01 = forms.CheckboxSelectMultiple(choices=OPTIONS)

    domanda02 = "I found the system unnecessarily complex."
    risposta02 = forms.MultipleChoiceField(choices=OPTIONS)

    domanda03 = "I thought the system was easy to use."
    risposta03 = forms.MultipleChoiceField(choices=OPTIONS)

    domanda04 = "I think that I would need the support of a technical person to be able to use this system."
    risposta04 = forms.MultipleChoiceField(choices=OPTIONS)

    domanda05 = "I found the various functions in this system were well integrated."
    risposta05 = forms.MultipleChoiceField(choices=OPTIONS)

    domanda06 = "I thought there was too much inconsistency in this system."
    risposta06 = forms.MultipleChoiceField(choices=OPTIONS)

    domanda07 = "I would imagine that most people would learn to use this system very quickly."
    risposta07 = forms.MultipleChoiceField(choices=OPTIONS)

    domanda08 = "I found the system very cumbersome to use."
    risposta08 = forms.MultipleChoiceField(choices=OPTIONS)

    domanda09 = "I felt very confident using the system."
    risposta09 = forms.MultipleChoiceField(choices=OPTIONS)

    domanda10 = "I needed to learn a lot of things before I could get going with this system."
    risposta10 = forms.MultipleChoiceField(choices=OPTIONS)