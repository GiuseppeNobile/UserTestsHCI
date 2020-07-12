from django import forms
from . import models
from .models import Form
from .models import Quesito
import csv



"""class SUSForm(forms.Form):

    nomeSUS = "SUS Form"

    OPTIONS = (('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5'))
 
    domanda01 = "I think that I would like to use this system frequently."
    risposta01 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda01)

    domanda02 = "I found the system unnecessarily complex."
    risposta02 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda02)
    
    domanda03 = "I thought the system was easy to use."
    risposta03 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda03)

    domanda04 = "I think that I would need the support of a technical person to be able to use this system."
    risposta04 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda04)

    domanda05 = "I found the various functions in this system were well integrated."
    risposta05 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda05)

    domanda06 = "I thought there was too much inconsistency in this system."
    risposta06 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda06)

    domanda07 = "I would imagine that most people would learn to use this system very quickly."
    risposta07 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda07)

    domanda08 = "I found the system very cumbersome to use."
    risposta08 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda08)

    domanda09 = "I felt very confident using the system."
    risposta09 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda09)

    domanda10 = "I needed to learn a lot of things before I could get going with this system."
    risposta10 = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect, label=domanda10)"""