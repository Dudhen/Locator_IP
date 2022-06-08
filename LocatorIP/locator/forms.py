from django import forms


class IPForm(forms.Form):
    IP = forms.CharField(label='IP', max_length=16)