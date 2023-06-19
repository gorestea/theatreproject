from django import forms
from .models import *

class AddPerformance(forms.ModelForm):
    class Meta:
        model = Performance
        fields = '__all__'

class GetEmail(forms.Form):
    email = forms.EmailField(max_length=255, label='Почтовый адрес:')
    name = forms.CharField(max_length=255, label='Имя пользователя:')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст сообщения:')

class Sendmail(forms.Form):
    email = forms.EmailField(max_length=255, label='Почтовый адрес:')