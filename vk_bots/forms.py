# -*- coding: utf-8 -*-
from django import forms

class Vk_discuss(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'сообщение для рассылки'}))
    login = forms.CharField(label='логин', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'логин VK'}))
    password = forms.CharField(label='пароль', max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}))
    photo = forms.CharField(label='медиа вложения(фото)', required=False)