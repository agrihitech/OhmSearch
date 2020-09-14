from django import forms
from django.contrib.admin import widgets
import os

CHOICE = [
('1', 'm ohm'),
('2', 'ohm'),
('3', 'k ohm'),
('4', 'M ohm'),
('5', 'G ohm')]

class SampleForm(forms.Form):
    value = forms.FloatField(min_value=0.0, max_value=1.0e9) 
    select = forms.ChoiceField(label='unit', widget=forms.Select, choices= CHOICE, initial=0)
    massege = ""
