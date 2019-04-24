from django import forms

class SenForm(forms.Form):
    sentence = forms.CharField()