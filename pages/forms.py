# pages/forms.py
from django import forms

class IlacForm(forms.Form):
    name = forms.CharField(label='İlaç Adı', max_length=100)
    purpose = forms.CharField(label='Kullanım Amacı', max_length=255)
    frequency = forms.CharField(label='Kullanım Sıklığı', max_length=255)
    how = forms.CharField(label='Nasıl Kullanılacak', max_length=255)
    kullanim = forms.CharField(label='Kullanım Sahası', max_length=255)
