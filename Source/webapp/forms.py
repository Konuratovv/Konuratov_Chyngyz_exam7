from django import forms
from django.forms import widgets


class NotesForms(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Имя автора")
    email = forms.EmailField(max_length=50, required=True, label="Email")
    text = forms.CharField(max_length=2000, required=True, label="Текст", widget=widgets.Textarea)
