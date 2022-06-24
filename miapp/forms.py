from django import forms


class posteo(forms.Form):
    #Especificar campos
    titulo = forms.CharField()
    sub_titulo = forms.CharField()
    cuerpo = forms.CharField()